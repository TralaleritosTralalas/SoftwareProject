from django.urls import reverse
from django.contrib.auth.models import Group
from app.tests.base import BaseTestSuite
from app.models import User


class TechAdminTest(BaseTestSuite):
    def setUp(self):
        super().setUp()
        self.tech_group, _ = Group.objects.get_or_create(name='technical')
        self.director_group, _ = Group.objects.get_or_create(name='director')

        self.user.role = self.tech_group
        self.user.save()
        self.client.login(username='tester', password=self.user_pwd)

    def test_access_denied_for_regular_user(self):
        self.user.role = None
        self.user.save()
        response = self.client.get('/tech/')
        self.assertEqual(response.status_code, 302)

    def test_access_granted_for_technical_role(self):
        response = self.client.get('/tech/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "System Administration")

    def test_tech_add_user_success(self):
        url = reverse('tech_admin:auth_user_add')
        data = {
            'username': 'new_worker',
            'first_name': 'Admin',
            'last_name': 'Test',
            'email': 'admin@test.com',
            'password': 'password123',
            'password_again': 'password123',
            'role': self.director_group.id
        }
        response = self.client.post(url, data)
        self.assertRedirects(response, reverse('tech_admin:index'))
        self.assertTrue(User.objects.filter(username='new_worker').exists())

    def test_tech_add_user_password_mismatch(self):
        url = reverse('tech_admin:auth_user_add')
        data = {
            'username': 'fail_user',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'fail@test.com',
            'password': 'pass1',
            'password_again': 'pass2',
            'role': self.director_group.id
        }
        self.client.post(url, data, follow=True)

        self.assertFalse(User.objects.filter(username='fail_user').exists())

    def test_tech_edit_user_data_and_password(self):
        target_user = User.objects.create_user(username='to_edit', password='old_password')
        url = reverse('tech_admin:auth_user_change', kwargs={'user_id': target_user.id})

        data = {
            'username': 'edited_user',
            'first_name': 'NewName',
            'last_name': 'NewLastName',
            'email': 'edited@test.com',
            'password': 'new_password123',
            'password_again': 'new_password123',
            'role': self.tech_group.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)

        target_user.refresh_from_db()
        self.assertEqual(target_user.username, 'edited_user')
        self.assertTrue(target_user.check_password('new_password123'))

    def test_tech_delete_user_success(self):
        target_user = User.objects.create_user(username='delete_me')
        url = reverse('tech_admin:auth_user_delete', kwargs={'user_id': target_user.id})
        response = self.client.post(url)
        self.assertRedirects(response, reverse('tech_admin:index'))
        self.assertFalse(User.objects.filter(id=target_user.id).exists())

    def test_tech_delete_self_prevention(self):
        url = reverse('tech_admin:auth_user_delete', kwargs={'user_id': self.user.id})
        response = self.client.post(url, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "TECH")
        self.assertContains(response, "DASHBOARD")
        self.assertTrue(User.objects.filter(id=self.user.id).exists())

    def test_tech_admin_search_logic(self):
        User.objects.create(username='unique_search_hit', email='target@test.com')
        response = self.client.get('/tech/', {'q': 'unique_search_hit'})
        self.assertContains(response, 'unique_search_hit')