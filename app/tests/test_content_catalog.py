from django.urls import reverse
from unittest.mock import patch
from app.tests.base import BaseTestSuite
from app.models import Movie, Genre, VisualizationProgress
import json


class ContentCatalogTest(BaseTestSuite):
    def setUp(self):
        super().setUp()
        self.genre = Genre.objects.create(name="Sci-Fi")
        self.movie = Movie.objects.create(
            title="Inception",
            synopsis="Dreams inside dreams",
            genre=self.genre,
            year=2010,
            release_date="2010-07-16",
            duration_minutes=148
        )
        self.content_id = "inception_2010"

        self.client.login(username='tester', password=self.user_pwd)

    @patch('app.views.get_all_movies')
    @patch('app.views.get_all_series')
    def test_catalog_view_renders(self, mock_series, mock_movies):
        mock_movies.return_value = [{'title': 'M1', 'unique_id': '1', 'genre_name': 'Sci-Fi'}]
        mock_series.return_value = []
        response = self.client.get(reverse('app:catalog'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/catalog.html')
        self.assertContains(response, 'M1')

    def test_search_empty_query(self):
        response = self.client.get(reverse('app:search'), {'q': ''})
        self.assertEqual(response.status_code, 200)

    @patch('app.services.search_content')
    def test_search_with_results(self, mock_search):
        mock_search.return_value = [
            {'title': 'Inception', 'unique_id': self.content_id, 'content_type': 'movie'}
        ]
        response = self.client.get(reverse('app:search'), {'q': 'Inception'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Inception')

    def test_catalog_filter_by_genre(self):
        response = self.client.get(reverse('app:catalog'), {'genre': self.genre.id})
        self.assertEqual(response.status_code, 200)

    def test_toggle_favorite_ajax(self):
        url = reverse('app:toggle_favorite', kwargs={'ctype': 'movie', 'cid': self.content_id})

        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(json.loads(response.content)['is_favorite'])

        response = self.client.post(url)
        self.assertFalse(json.loads(response.content)['is_favorite'])

    def test_update_visualization_status(self):
        url = reverse('app:update_status', kwargs={'ctype': 'movie', 'cid': self.content_id})
        data = json.dumps({'status': 'completed'})

        response = self.client.post(url, data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content)['status'], 'completed')

        progress = VisualizationProgress.objects.get(user=self.user, content__title="Inception")
        self.assertTrue(progress.completed)

    def test_content_detail_404(self):
        url = reverse('app:content_detail', kwargs={'ctype': 'movie', 'cid': 'non-existent-id'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_unauthenticated_user_redirect(self):
        self.client.logout()
        url = reverse('app:toggle_favorite', kwargs={'ctype': 'movie', 'cid': self.content_id})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse('login'), response.url)