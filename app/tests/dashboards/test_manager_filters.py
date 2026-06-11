from django.urls import reverse
from django.contrib.auth.models import Group
from app.models import Statistics, Genre, Platform, Movie
from app.tests.base import BaseTestSuite
from django.utils import timezone
from datetime import timedelta


class ManagerDashboardFiltersTest(BaseTestSuite):
    def setUp(self):
        super().setUp()
        self.manager_group, _ = Group.objects.get_or_create(name='manager')
        self.user.role = self.manager_group
        self.user.save()
        self.client.login(username='tester', password=self.user_pwd)

        self.genre = Genre.objects.create(name="Comedy")
        self.p1 = Platform.objects.create(platform_name="Platform 1", p_manager=self.user)
        self.movie = Movie.objects.create(
            title="Succession",
            genre=self.genre,
            year=2021,
            release_date=timezone.now().date(),
            duration_minutes=60
        )

        self.stats = Statistics.objects.create(
            platform=self.p1,
            total_clicks=100,
            total_favorites=50,
            week=timezone.now().date()
        )

    def test_manager_dashboard_filter_by_range_24h(self):
        response = self.client.get(reverse('app:manager_dashboard'), {'range': '24h'})
        self.assertEqual(response.status_code, 200)

    def test_manager_dashboard_filter_by_range_7d(self):
        Statistics.objects.create(
            platform=self.p1,
            total_clicks=500,
            total_favorites=250,
            week=timezone.now().date() - timedelta(days=5)
        )

        response = self.client.get(reverse('app:manager_dashboard'), {'range': '7d'})
        self.assertEqual(response.status_code, 200)

    def test_manager_dashboard_custom_date_range(self):
        start = (timezone.now() - timedelta(days=10)).strftime('%Y-%m-%d')
        end = timezone.now().strftime('%Y-%m-%d')

        response = self.client.get(reverse('app:manager_dashboard'), {
            'start_date': start,
            'end_date': end
        })
        self.assertEqual(response.status_code, 200)
