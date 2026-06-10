from django.urls import reverse
from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory
from app.tests.base import BaseTestSuite
from app.models import Movie, Genre, Favorite, User
from app.views import toggle_favorite
import json


class FavoritesTest(BaseTestSuite):
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

    def test_toggle_favorite_ajax(self):
        url = reverse('app:toggle_favorite', kwargs={'ctype': 'movie', 'cid': self.content_id})

        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(json.loads(response.content)['is_favorite'])

        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(json.loads(response.content)['is_favorite'])

    def test_superuser_cannot_favorite(self):
        # Create a superuser
        superuser = User.objects.create_superuser(username='super', email='s@s.com', password=self.user_pwd)
        self.client.login(username='super', password=self.user_pwd)
        url = reverse('app:toggle_favorite', kwargs={'ctype': 'movie', 'cid': self.content_id})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 403)
        self.assertIn('Superusers cannot have favorites', json.loads(response.content)['message'])

    def test_unauthenticated_user_redirect_client(self):
        self.client.logout()
        url = reverse('app:toggle_favorite', kwargs={'ctype': 'movie', 'cid': self.content_id})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse('login'), response.url)

    def test_unauthenticated_user_returns_401_directly(self):
        # Using RequestFactory to bypass the customer_only redirect decorator
        factory = RequestFactory()
        request = factory.post(reverse('app:toggle_favorite', kwargs={'ctype': 'movie', 'cid': self.content_id}))
        request.user = AnonymousUser()
        
        # Call the underlying wrapped view function directly
        # Since toggle_favorite is decorated with @customer_only, we can call toggle_favorite.__wrapped__
        # to test the internal view logic directly!
        response = toggle_favorite.__wrapped__(request, ctype='movie', cid=self.content_id)
        self.assertEqual(response.status_code, 401)
        data = json.loads(response.content)
        self.assertEqual(data['status'], 'error')
        self.assertEqual(data['message'], 'Authentication required')
