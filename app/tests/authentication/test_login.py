from django.urls import reverse
from app.tests.base import BaseTestSuite


class LoginTest(BaseTestSuite):
    def test_login_valid_user(self):
        response = self.client.post(reverse('login'), {
            'username': 'tester',
            'password': self.user_pwd
        })
        self.assertEqual(response.status_code, 302)
        self.assertIn('/redirect/', response.url)

    def test_login_wrong_username(self):
        response = self.client.post(reverse('login'), {
            'username': 'not_tester',
            'password': self.user_pwd
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Invalid")

    def test_login_wrong_password(self):
        response = self.client.post(reverse('login'), {
            'username': 'tester',
            'password': 'incorrect_password'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Invalid")

    def test_redirect_to_onboarding_if_not_completed(self):
        self.user.onboarding_completed = False
        self.user.save()

        self.client.login(username='tester', password=self.user_pwd)

        response = self.client.get(reverse('app:login_redirect'))

        self.assertRedirects(response, reverse('app:onboarding'))

    def test_redirect_to_main_if_onboarding_completed(self):
        self.user.onboarding_completed = True
        self.user.save()

        self.client.login(username='tester', password=self.user_pwd)

        response = self.client.get(reverse('app:login_redirect'))

        self.assertRedirects(response, reverse('app:main'))
