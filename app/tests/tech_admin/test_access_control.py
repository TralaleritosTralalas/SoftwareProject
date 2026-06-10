from django.urls import reverse
from django.contrib.auth.models import Group
from app.tests.base import BaseTestSuite


class TechAccessControlTest(BaseTestSuite):
    def setUp(self):
        super().setUp()
        self.tech_group, _ = Group.objects.get_or_create(name='technical')
        self.user.role = self.tech_group
        self.user.save()
        self.client.login(username='tester', password=self.user_pwd)

    def test_access_denied_for_regular_user(self):
        self.user.role = None
        self.user.save()
        
        # When regular user tries to access reverse('tech_admin:index'), it redirects to login
        response = self.client.get(reverse('tech_admin:index'))
        self.assertEqual(response.status_code, 302)

    def test_access_granted_for_technical_role(self):
        response = self.client.get(reverse('tech_admin:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "System Administration")
