from django.urls import reverse
from app.models import User
from app.tests.base import BaseTestSuite


class LoginTest(BaseTestSuite):
    def test_login_valid_user(self):
        response = self.client.post(reverse('login'), {
            'username': 'tester',
            'password': self.user_pwd
        })
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse('app:login_redirect'), response.url)

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


class RegisterTest(BaseTestSuite):
    def test_registration_success_creates_user(self):
        response = self.client.post(reverse('signup'), {
            'username': 'new_user_unique',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'new_unique@test.com',
            'password1': 'SecurePass123!',
            'password2': 'SecurePass123!',
            'terms_of_service': True,
            'privacy_policy': True
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='new_user_unique').exists())

    def test_registration_duplicate_username(self):
        data = {
            'username': 'tester',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'different@test.com',
            'password1': 'SecurePass123!',
            'password2': 'SecurePass123!',
            'terms_of_service': True,
            'privacy_policy': True
        }
        response = self.client.post(reverse('signup'), data)
        self.assertEqual(response.status_code, 200)
        form = response.context.get('form')
        self.assertIn('username', form.errors)
        self.assertEqual(form.errors['username'], ['A user with that username already exists.'])

    def test_registration_password_bad_duplicated(self):
        data = {
            'username': 'tester2',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'different@test.com',
            'password1': 'SecurePass123!',
            'password2': 'SecurePass123!_bad',
            'terms_of_service': True,
            'privacy_policy': True
        }
        response = self.client.post(reverse('signup'), data)
        self.assertEqual(response.status_code, 200)
        form = response.context.get('form')
        self.assertIn('password2', form.errors)
        self.assertEqual(form.errors['password2'], ["The two password fields didn't match."])

    def test_registration_bad_email(self):
        data = {
            'username': 'tester2',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'test',
            'password1': 'SecurePass123!',
            'password2': 'SecurePass123!_bad',
            'terms_of_service': True,
            'privacy_policy': True
        }
        response = self.client.post(reverse('signup'), data)
        self.assertEqual(response.status_code, 200)
        form = response.context.get('form')
        self.assertIn('email', form.errors)
        self.assertEqual(form.errors['email'], ["Enter a valid email address."])


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
