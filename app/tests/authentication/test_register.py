from django.urls import reverse
from app.models import User
from app.tests.base import BaseTestSuite


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
