from django.urls import reverse
from app.tests.base import BaseTestSuite


class LogoutSuccessTest(BaseTestSuite):
    def test_logout_redirects_to_home(self):
        self.client.login(username='tester', password=self.user_pwd)
        self.assertIn('_auth_user_id', self.client.session)
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, 302)
        self.assertNotIn('_auth_user_id', self.client.session)
        self.assertRedirects(response, reverse('app:home'))

    def test_logout_without_login(self):
        self.client.logout()
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, 302)
        self.assertNotIn('_auth_user_id', self.client.session)
