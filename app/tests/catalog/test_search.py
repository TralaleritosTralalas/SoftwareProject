from django.urls import reverse
from unittest.mock import patch
from app.tests.base import BaseTestSuite
from app.models import Movie, Director, Genre


class SearchViewTest(BaseTestSuite):
    def setUp(self):
        super().setUp()
        self.genre = Genre.objects.create(name="Sci-Fi")
        self.director = Director.objects.create(name="Christopher Nolan", birth_date="1970-07-30")
        self.movie = Movie.objects.create(
            title="Inception",
            synopsis="Dreams inside dreams",
            genre=self.genre,
            director=self.director,
            year=2010,
            release_date="2010-07-16",
            duration_minutes=148
        )
        self.client.login(username='tester', password=self.user_pwd)

    def test_search_empty_query(self):
        response = self.client.get(reverse('app:search'), {'q': ''})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/search.html')

    def test_search_by_title_match(self):
        response = self.client.get(reverse('app:search'), {'q': 'Incept'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Inception')

    def test_search_by_director_match(self):
        response = self.client.get(reverse('app:search'), {'q': 'Nolan'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Inception')

    @patch('app.views.search_content')
    def test_search_with_mocked_results(self, mock_search):
        mock_search.return_value = [
            {'title': 'Mocked Movie', 'unique_id': 'mocked_2022', 'content_type': 'movie', 'genre_name': 'Sci-Fi'}
        ]
        response = self.client.get(reverse('app:search'), {'q': 'anything'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Mocked Movie')
