from django.urls import reverse
from app.models import Genre, Country
from app.tests.base import BaseTestSuite

class OnboardingTest(BaseTestSuite):
    def setUp(self):
        super().setUp()
        self.country = Country.objects.create(name="Spain", iso_code="ES")
        self.g1 = Genre.objects.create(name="Action")
        self.g2 = Genre.objects.create(name="Comedy")
        self.g3 = Genre.objects.create(name="Drama")
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

    def test_onboarding_genres_minimum_validation(self):
        self.user.onboarding_completed = True
        self.user.save()

        response = self.client.post(reverse('app:onboarding_genres'), {
            'genres': [self.g1.id, self.g2.id]
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Select at least 3 genres")

    def test_onboarding_genres_success(self):
        self.user.onboarding_completed = True
        self.user.save()

        response = self.client.post(reverse('app:onboarding_genres'), {
            'genres': [self.g1.id, self.g2.id, self.g3.id]
        })
        self.assertRedirects(response, reverse('app:onboarding_complete'))
        self.assertEqual(self.user.favorite_genres.count(), 3)

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