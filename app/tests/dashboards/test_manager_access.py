from django.urls import reverse
from django.contrib.auth.models import Group
from app.tests.base import BaseTestSuite


class ManagerDashboardAccessTest(BaseTestSuite):
    def setUp(self):
        super().setUp()
        self.manager_group, _ = Group.objects.get_or_create(name='manager')

    def test_access_denied_for_regular_user(self):
        self.client.login(username='tester', password=self.user_pwd)
        response = self.client.get(reverse('app:manager_dashboard'))
        self.assertEqual(response.status_code, 403)

    def test_access_granted_for_manager(self):
        self.user.role = self.manager_group
        self.user.save()
        self.client.login(username='tester', password=self.user_pwd)

        response = self.client.get(reverse('app:manager_dashboard'))
        self.assertEqual(response.status_code, 200)

    def test_access_redirects_unauthenticated(self):
        self.client.logout()
        response = self.client.get(reverse('app:manager_dashboard'))
        self.assertEqual(response.status_code, 302)
