from django.urls import reverse
from django.contrib.auth.models import Group
from app.models import Statistics, Genre, Platform, Movie, Favorite
from app.tests.base import BaseTestSuite
from django.utils import timezone


class DirectionDashboardChartsTest(BaseTestSuite):
    def setUp(self):
        super().setUp()
        self.director_group, _ = Group.objects.get_or_create(name='director')
        self.user.role = self.director_group
        self.user.save()
        self.client.login(username='tester', password=self.user_pwd)

        self.genre = Genre.objects.create(name="Drama")
        self.p1 = Platform.objects.create(platform_name="Platform 1", p_manager=self.user)
        self.p2 = Platform.objects.create(platform_name="Platform 2", p_manager=self.user)

        self.movie = Movie.objects.create(
            title="Succession",
            genre=self.genre,
            year=2021,
            release_date=timezone.now().date(),
            duration_minutes=60
        )

        Statistics.objects.create(
            platform=self.p1,
            total_clicks=100,
            total_favorites=50,
            week=timezone.now().date()
        )

    def test_export_csv_is_valid(self):
        response = self.client.get(reverse('app:direction_dashboard'), {'export': 'csv'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'text/csv')

    def test_dashboard_top_performing_platform(self):
        Statistics.objects.create(
            platform=self.p2,
            total_clicks=1000,
            total_favorites=100,
            week=timezone.now().date()
        )

        response = self.client.get(reverse('app:direction_dashboard'))
        self.assertContains(response, "Platform 2")

    def test_dashboard_trending_content_list(self):
        Favorite.objects.create(user=self.user, content=self.movie)

        response = self.client.get(reverse('app:direction_dashboard'))
        self.assertContains(response, "Succession")

    def test_dashboard_chart_data_presence(self):
        response = self.client.get(reverse('app:direction_dashboard'))
        self.assertIn('chart_labels', response.context)
        self.assertIn('chart_values', response.context)
