from django.urls import reverse
from django.contrib.auth.models import Group
from app.models import Statistics, Genre, Platform, Movie, Favorite
from app.tests.base import BaseTestSuite
from django.utils import timezone
from datetime import timedelta


class DirectionDashboardTest(BaseTestSuite):
    def setUp(self):
        super().setUp()
        self.director_group, _ = Group.objects.get_or_create(name='director')
        self.genre = Genre.objects.create(name="Drama")

        self.p1 = Platform.objects.create(
            platform_name="Platform 1",
            p_manager=self.user
        )

        self.p2 = Platform.objects.create(
            platform_name="Platform 2",
            p_manager=self.user
        )

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

    def test_access_denied_for_regular_user(self):
        self.client.login(username='tester', password=self.user_pwd)
        response = self.client.get(reverse('app:direction_dashboard'))
        self.assertEqual(response.status_code, 403)

    def test_access_granted_for_director(self):
        self.user.role = self.director_group
        self.user.save()
        self.client.login(username='tester', password=self.user_pwd)

        response = self.client.get(reverse('app:direction_dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "100")

    def test_export_csv_is_valid(self):
        self.user.role = self.director_group
        self.user.save()
        self.client.login(username='tester', password=self.user_pwd)

        response = self.client.get(reverse('app:direction_dashboard'), {'export': 'csv'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'text/csv')

    def test_dashboard_filter_by_range_24h(self):
        self.user.role = self.director_group
        self.user.save()
        self.client.login(username='tester', password=self.user_pwd)

        response = self.client.get(reverse('app:direction_dashboard'), {'range': '24h'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "100")

    def test_dashboard_filter_by_range_7d(self):
        self.user.role = self.director_group
        self.user.save()
        self.client.login(username='tester', password=self.user_pwd)

        Statistics.objects.create(
            platform=self.p1,
            total_clicks=500,
            total_favorites=250,
            week=timezone.now().date() - timedelta(days=5)
        )

        response = self.client.get(reverse('app:direction_dashboard'), {'range': '7d'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "600")

    def test_dashboard_custom_date_range(self):
        self.user.role = self.director_group
        self.user.save()
        self.client.login(username='tester', password=self.user_pwd)

        start = (timezone.now() - timedelta(days=10)).strftime('%Y-%m-%d')
        end = timezone.now().strftime('%Y-%m-%d')

        response = self.client.get(reverse('app:direction_dashboard'), {
            'start_date': start,
            'end_date': end
        })
        self.assertEqual(response.status_code, 200)

    def test_dashboard_empty_statistics(self):
        Statistics.objects.all().delete()
        self.user.role = self.director_group
        self.user.save()
        self.client.login(username='tester', password=self.user_pwd)

        response = self.client.get(reverse('app:direction_dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "0")

    def test_dashboard_top_performing_platform(self):
        self.user.role = self.director_group
        self.user.save()
        self.client.login(username='tester', password=self.user_pwd)

        Statistics.objects.create(
            platform=self.p2,
            total_clicks=1000,
            total_favorites=100,
            week=timezone.now().date()
        )

        response = self.client.get(reverse('app:direction_dashboard'))
        self.assertContains(response, "Platform 2")

    def test_dashboard_trending_content_list(self):
        self.user.role = self.director_group
        self.user.save()
        self.client.login(username='tester', password=self.user_pwd)

        Favorite.objects.create(user=self.user, content=self.movie)

        response = self.client.get(reverse('app:direction_dashboard'))
        self.assertContains(response, "Succession")

    def test_dashboard_chart_data_presence(self):
        self.user.role = self.director_group
        self.user.save()
        self.client.login(username='tester', password=self.user_pwd)

        response = self.client.get(reverse('app:direction_dashboard'))
        self.assertIn('chart_labels', response.context)
        self.assertIn('chart_values', response.context)