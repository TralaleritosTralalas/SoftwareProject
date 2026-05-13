from django.urls import reverse
from app.tests.base import BaseTestSuite
from app.models import User, Country

class UserProfileTest(BaseTestSuite):
    def setUp(self):
        super().setUp()
        self.test_country = Country.objects.create(name="United States")
        self.client.login(username='tester', password=self.user_pwd)

    def test_update_profile_info_success(self):
        response = self.client.post(reverse('app:user_settings'), {
            'action': 'update_profile',
            'username': 'tester_updated',
            'first_name': 'NewName',
            'last_name': 'NewLastName',
            'bio': 'This is my new bio',
            'gender': 'M',
            'country': self.test_country.id
        })
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, 'tester_updated')
        self.assertEqual(self.user.first_name, 'NewName')
        self.assertEqual(self.user.country, self.test_country)
        self.assertContains(response, "Profile updated successfully!")

    def test_update_profile_duplicate_username(self):
        User.objects.create_user(username='other_user', password='password123')
        response = self.client.post(reverse('app:user_settings'), {
            'action': 'update_profile',
            'username': 'other_user',
            'first_name': 'Test',
            'last_name': 'User'
        })
        self.assertContains(response, "Username already exists")
        self.user.refresh_from_db()
        self.assertNotEqual(self.user.username, 'other_user')

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

    def test_update_profile_missing_required_fields(self):
        response = self.client.post(reverse('app:user_settings'), {
            'action': 'update_profile',
            'username': '',
            'first_name': '',
            'last_name': ''
        })
        self.assertContains(response, "Username is required")
        self.assertContains(response, "First name is required")
        self.assertContains(response, "Last name is required")