from django.urls import reverse
from app.models import Country
from app.tests.base import BaseTestSuite


class OnboardingProfileStepTest(BaseTestSuite):
    def setUp(self):
        super().setUp()
        self.country = Country.objects.create(name="Spain", iso_code="ES")
        self.client.login(username='tester', password=self.user_pwd)

    def test_onboarding_step_1_success(self):
        response = self.client.post(reverse('app:onboarding'), {
            'birth_date': '1990-01-01',
            'country': self.country.id,
            'gender': 'male'
        })
        self.user.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertTrue(self.user.onboarding_completed)
        self.assertRedirects(response, reverse('app:onboarding_genres'))

    def test_access_onboarding_when_already_completed(self):
        self.user.onboarding_completed = True
        self.user.save()

        response = self.client.get(reverse('app:onboarding'))
        self.assertRedirects(response, reverse('app:main'))

    def test_onboarding_unauthenticated_redirect(self):
        self.client.logout()
        response = self.client.get(reverse('app:onboarding'))
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse('login'), response.url)
