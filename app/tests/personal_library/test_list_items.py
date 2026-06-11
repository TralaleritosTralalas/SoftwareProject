from django.urls import reverse
from app.tests.base import BaseTestSuite
from app.models import Movie, Genre, Watchlist
import json


class WatchlistItemsDuplicatePreventionTest(BaseTestSuite):
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
        self.watchlist = Watchlist.objects.create(user=self.user, name="My List")
        self.client.login(username='tester', password=self.user_pwd)

    def test_adding_duplicate_items_prevented(self):
        url = reverse('app:add_to_list', kwargs={
            'ctype': 'movie',
            'cid': self.content_id,
            'list_id': self.watchlist.id
        })
        
        # Add first time
        response1 = self.client.post(url)
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(json.loads(response1.content)['item_count'], 1)
        
        # Add second time
        response2 = self.client.post(url)
        self.assertEqual(response2.status_code, 200)
        self.assertEqual(json.loads(response2.content)['item_count'], 1)
        
        # Verify database junction count is exactly 1
        self.assertEqual(self.watchlist.content.count(), 1)
