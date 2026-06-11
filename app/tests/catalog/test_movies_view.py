from django.urls import reverse
from unittest.mock import patch
from app.tests.base import BaseTestSuite


class MoviesViewTest(BaseTestSuite):
    @patch('app.views.get_all_movies')
    @patch('app.views.get_all_platforms')
    @patch('app.views.get_all_genres_from_api')
    def test_movies_view_basic(self, mock_genres, mock_platforms, mock_movies):
        mock_movies.return_value = [
            {'title': 'Movie A', 'unique_id': 'a', 'genre_name': 'Action', 'rating': 8.5, 'year': 2020},
            {'title': 'Movie B', 'unique_id': 'b', 'genre_name': 'Comedy', 'rating': 7.0, 'year': 2019},
        ]
        mock_platforms.return_value = []
        mock_genres.return_value = []

        # Access movies page
        response = self.client.get(reverse('app:movies'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Movie A')
        self.assertContains(response, 'Movie B')

    @patch('app.views.get_all_movies')
    @patch('app.views.get_all_platforms')
    @patch('app.views.get_all_genres_from_api')
    def test_movies_view_filter_and_sort(self, mock_genres, mock_platforms, mock_movies):
        mock_movies.return_value = [
            {'title': 'Movie A', 'unique_id': 'a', 'genre_name': 'Action', 'rating': 8.5, 'year': 2020},
            {'title': 'Movie B', 'unique_id': 'b', 'genre_name': 'Comedy', 'rating': 7.0, 'year': 2019},
        ]
        mock_platforms.return_value = []
        mock_genres.return_value = []

        # Filter by genre Action
        response = self.client.get(reverse('app:movies'), {'genre': 'Action'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Movie A')
        self.assertNotContains(response, 'Movie B')

        # Sort by rating asc
        response = self.client.get(reverse('app:movies'), {'sort_rating': 'asc'})
        self.assertEqual(response.status_code, 200)

        # Sort by year desc
        response = self.client.get(reverse('app:movies'), {'sort_year': 'desc'})
        self.assertEqual(response.status_code, 200)
