from django.urls import reverse
from unittest.mock import patch
from django.contrib.auth.models import Group
from app.tests.base import BaseTestSuite
from app.models import Genre


class CatalogViewTest(BaseTestSuite):
    def setUp(self):
        super().setUp()
        self.genre = Genre.objects.create(name="Sci-Fi")

    @patch('app.views.get_all_movies')
    @patch('app.views.get_all_series')
    def test_catalog_view_renders_authenticated_customer(self, mock_series, mock_movies):
        mock_movies.return_value = [{'title': 'M1', 'unique_id': '1', 'genre_name': 'Sci-Fi'}]
        mock_series.return_value = []
        self.client.login(username='tester', password=self.user_pwd)
        response = self.client.get(reverse('app:catalog'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/catalog.html')
        self.assertContains(response, 'M1')

    @patch('app.views.get_all_movies')
    @patch('app.views.get_all_series')
    def test_catalog_view_renders_unauthenticated_guest(self, mock_series, mock_movies):
        mock_movies.return_value = [{'title': 'Guest Movie', 'unique_id': '1', 'genre_name': 'Sci-Fi'}]
        mock_series.return_value = []
        self.client.logout()
        response = self.client.get(reverse('app:catalog'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/catalog.html')
        self.assertContains(response, 'Guest Movie')

    def test_catalog_view_denied_for_staff_roles(self):
        # Create a director/staff user and ensure they cannot access
        director_group, _ = Group.objects.get_or_create(name='director')
        self.user.role = director_group
        self.user.save()
        self.client.login(username='tester', password=self.user_pwd)
        response = self.client.get(reverse('app:catalog'))
        self.assertEqual(response.status_code, 403)

    def test_catalog_filter_by_genre(self):
        self.client.login(username='tester', password=self.user_pwd)
        response = self.client.get(reverse('app:catalog'), {'genre': self.genre.id})
        self.assertEqual(response.status_code, 200)
