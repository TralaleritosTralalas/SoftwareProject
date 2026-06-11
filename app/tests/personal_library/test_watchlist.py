from django.urls import reverse
from app.tests.base import BaseTestSuite
from app.models import Movie, Genre, Watchlist
import json


class WatchlistOperationsTest(BaseTestSuite):
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
        self.watchlist = Watchlist.objects.create(user=self.user, name="Watchlist 1")
        self.client.login(username='tester', password=self.user_pwd)

    def test_add_to_list_success(self):
        url = reverse('app:add_to_list', kwargs={
            'ctype': 'movie',
            'cid': self.content_id,
            'list_id': self.watchlist.id
        })
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue(data['success'])
        self.assertEqual(data['item_count'], 1)
        self.assertTrue(self.watchlist.content.filter(id=self.movie.id).exists())

    def test_add_to_list_nonexistent_list(self):
        url = reverse('app:add_to_list', kwargs={
            'ctype': 'movie',
            'cid': self.content_id,
            'list_id': 99999
        })
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertFalse(data['success'])
        self.assertEqual(data['error'], 'List not found')

    def test_remove_from_list_success(self):
        self.watchlist.content.add(self.movie)
        url = reverse('app:remove_from_list', kwargs={
            'ctype': 'movie',
            'cid': self.content_id,
            'list_id': self.watchlist.id
        })
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue(data['success'])
        self.assertEqual(data['item_count'], 0)
        self.assertFalse(self.watchlist.content.filter(id=self.movie.id).exists())

    def test_list_detail_success(self):
        self.watchlist.content.add(self.movie)
        url = reverse('app:list_detail', kwargs={'list_id': self.watchlist.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/list_detail.html')
        self.assertContains(response, 'Inception')

    def test_list_detail_404_nonexistent(self):
        url = reverse('app:list_detail', kwargs={'list_id': 99999})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
