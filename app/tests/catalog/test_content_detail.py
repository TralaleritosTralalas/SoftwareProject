from django.urls import reverse
from unittest.mock import patch
from app.tests.base import BaseTestSuite
from app.models import Movie, Genre


class ContentDetailViewTest(BaseTestSuite):
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
    def test_content_detail_success(self, mock_movies):
        mock_movies.return_value = [
            {'title': 'Inception', 'year': 2010, 'unique_id': self.content_id, 'id': 1}
        ]
        url = reverse('app:content_detail', kwargs={'ctype': 'movie', 'cid': self.content_id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/content_view.html')
        self.assertContains(response, 'Inception')

    def test_content_detail_404(self):
        url = reverse('app:content_detail', kwargs={'ctype': 'movie', 'cid': 'non-existent-id'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, 'pages/main.html')
