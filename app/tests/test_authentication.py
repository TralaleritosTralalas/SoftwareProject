from django.urls import reverse
from app.models import User
from app.tests.base import BaseTestSuite
from django.core import mail
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.utils import timezone


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


class PasswordResetTests(BaseTestSuite):
    def setUp(self):
        super().setUp()
        self.uid = urlsafe_base64_encode(force_bytes(self.user.pk))
        self.token = default_token_generator.make_token(self.user)
        self.reset_confirm_url = reverse('password_reset_confirm', kwargs={
            'uidb64': self.uid,
            'token': self.token
        })

    def test_password_reset_email_sent(self):
        response = self.client.post(reverse('password_reset'), {
            'email': self.user.email
        })
        self.assertRedirects(response, reverse('password_reset_done'))
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn("Password reset", mail.outbox[0].subject)

    def test_password_reset_invalid_email(self):
        self.client.post(reverse('password_reset'), {'email': 'unknown@gmail.com'})
        self.assertEqual(len(mail.outbox), 0)

    def test_password_reset_confirm_view_loads(self):
        response = self.client.get(self.reset_confirm_url, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "New Password")

    def test_password_reset_success(self):
        self.client.logout()
        self.user.set_password('temporal_password')
        self.user.last_login = timezone.now().replace(microsecond=0)
        self.user.save()
        old_hash = self.user.password
        uid = urlsafe_base64_encode(force_bytes(self.user.pk))
        token = default_token_generator.make_token(self.user)
        response_get = self.client.get(
            reverse('password_reset_confirm', kwargs={'uidb64': uid, 'token': token}),
            follow=True
        )
        post_url = response_get.redirect_chain[-1][0] if response_get.redirect_chain else response_get.request[
            'PATH_INFO']
        new_pwd = "SecurePassed235!!!!"
        response = self.client.post(post_url, {
            'new_password1': new_pwd,
            'new_password2': new_pwd,
        }, follow=True)
        self.user.refresh_from_db()
        self.assertNotEqual(old_hash, self.user.password)
        self.assertTrue(self.user.check_password(new_pwd))
        self.assertContains(response, "Password Updated!")

    def test_password_reset_mismatch(self):
        response = self.client.post(self.reset_confirm_url, {
            'new_password1': 'SecurePass234!',
            'new_password2': 'SecurePassed235!!!!'
        }, follow=True)
        self.assertContains(response, "match")

    def test_password_reset_too_common(self):
        response = self.client.post(self.reset_confirm_url, {
            'new_password1': 'password123',
            'new_password2': 'password123'
        }, follow=True)
        self.assertContains(response, "common")

    def test_password_reset_invalid_token(self):
        bad_url = reverse('password_reset_confirm', kwargs={
            'uidb64': self.uid,
            'token': 'false_token'
        })
        response = self.client.get(bad_url, follow=True)
        self.assertContains(response, "Link Expired")
