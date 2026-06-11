from django.urls import reverse
from unittest.mock import patch
from app.tests.base import BaseTestSuite


class SeriesViewTest(BaseTestSuite):
    @patch('app.views.get_all_series')
    @patch('app.views.get_all_platforms')
    @patch('app.views.get_all_genres_from_api')
    def test_series_view_basic(self, mock_genres, mock_platforms, mock_series):
        mock_series.return_value = [
            {'title': 'Series A', 'unique_id': 'a', 'genre_name': 'Drama', 'rating': 9.0, 'start_year': 2018},
            {'title': 'Series B', 'unique_id': 'b', 'genre_name': 'Comedy', 'rating': 7.5, 'start_year': 2021},
        ]
        mock_platforms.return_value = []
        mock_genres.return_value = []

        response = self.client.get(reverse('app:series'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Series A')
        self.assertContains(response, 'Series B')

    @patch('app.views.get_all_series')
    @patch('app.views.get_all_platforms')
    @patch('app.views.get_all_genres_from_api')
    def test_series_view_filter_and_sort(self, mock_genres, mock_platforms, mock_series):
        mock_series.return_value = [
            {'title': 'Series A', 'unique_id': 'a', 'genre_name': 'Drama', 'rating': 9.0, 'start_year': 2018},
            {'title': 'Series B', 'unique_id': 'b', 'genre_name': 'Comedy', 'rating': 7.5, 'start_year': 2021},
        ]
        mock_platforms.return_value = []
        mock_genres.return_value = []

        response = self.client.get(reverse('app:series'), {'genre': 'Drama'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Series A')
        self.assertNotContains(response, 'Series B')

        response = self.client.get(reverse('app:series'), {'sort_rating': 'asc'})
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse('app:series'), {'sort_year': 'desc'})
        self.assertEqual(response.status_code, 200)
