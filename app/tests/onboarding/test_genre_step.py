from django.urls import reverse
from app.models import Genre
from app.tests.base import BaseTestSuite


class OnboardingGenreStepTest(BaseTestSuite):
    def setUp(self):
        super().setUp()
        self.g1 = Genre.objects.create(name="Action")
        self.g2 = Genre.objects.create(name="Comedy")
        self.g3 = Genre.objects.create(name="Drama")
        self.client.login(username='tester', password=self.user_pwd)

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
