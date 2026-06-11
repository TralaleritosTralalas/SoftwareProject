from django.urls import reverse
from app.models import User
from app.tests.base import BaseTestSuite
from django.core import mail
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.utils import timezone


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
