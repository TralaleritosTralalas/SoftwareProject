from django.urls import reverse
from app.tests.base import BaseTestSuite


class UserPasswordChangeTest(BaseTestSuite):
    def setUp(self):
        super().setUp()
        self.client.login(username='tester', password=self.user_pwd)

    def test_change_password_success(self):
        response = self.client.post(reverse('app:user_settings'), {
            'action': 'change_password',
            'current_password': self.user_pwd,
            'new_password': 'NewPassword123!',
            'confirm_password': 'NewPassword123!'
        })
        self.assertContains(response, "Password changed successfully!")
        self.client.logout()
        login_success = self.client.login(username='tester', password='NewPassword123!')
        self.assertTrue(login_success)

    def test_change_password_wrong_current(self):
        response = self.client.post(reverse('app:user_settings'), {
            'action': 'change_password',
            'current_password': 'wrong_password',
            'new_password': 'NewPassword123!',
            'confirm_password': 'NewPassword123!'
        })
        self.assertContains(response, "Current password is incorrect")

    def test_change_password_mismatch(self):
        response = self.client.post(reverse('app:user_settings'), {
            'action': 'change_password',
            'current_password': self.user_pwd,
            'new_password': 'NewPassword123!',
            'confirm_password': 'DifferentPassword123!'
        })
        self.assertContains(response, "New password and confirm password do not match")

    def test_change_password_too_short(self):
        response = self.client.post(reverse('app:user_settings'), {
            'action': 'change_password',
            'current_password': self.user_pwd,
            'new_password': '123',
            'confirm_password': '123'
        })
        self.assertContains(response, "New password must be at least 8 characters")
