from django.urls import reverse
from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory
from app.tests.base import BaseTestSuite
from app.models import Movie, Genre, VisualizationProgress, User
from app.views import update_status
import json


class VisualizationProgressTest(BaseTestSuite):
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

    def test_update_visualization_status_completed(self):
        url = reverse('app:update_status', kwargs={'ctype': 'movie', 'cid': self.content_id})
        data = json.dumps({'status': 'completed'})

        response = self.client.post(url, data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content)['status'], 'completed')

        progress = VisualizationProgress.objects.get(user=self.user, content=self.movie)
        self.assertTrue(progress.completed)

    def test_update_visualization_status_watching(self):
        url = reverse('app:update_status', kwargs={'ctype': 'movie', 'cid': self.content_id})
        data = json.dumps({'status': 'watching'})

        response = self.client.post(url, data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content)['status'], 'watching')

        progress = VisualizationProgress.objects.get(user=self.user, content=self.movie)
        self.assertFalse(progress.completed)
        self.assertEqual(progress.last_minute, 1)

    def test_superuser_cannot_track_status(self):
        superuser = User.objects.create_superuser(username='super', email='s@s.com', password=self.user_pwd)
        self.client.login(username='super', password=self.user_pwd)
        url = reverse('app:update_status', kwargs={'ctype': 'movie', 'cid': self.content_id})
        data = json.dumps({'status': 'completed'})
        response = self.client.post(url, data, content_type='application/json')
        self.assertEqual(response.status_code, 403)
        self.assertIn('Superusers cannot track watch status', json.loads(response.content)['message'])

    def test_unauthenticated_user_redirect_client(self):
        self.client.logout()
        url = reverse('app:update_status', kwargs={'ctype': 'movie', 'cid': self.content_id})
        data = json.dumps({'status': 'completed'})
        response = self.client.post(url, data, content_type='application/json')
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse('login'), response.url)

    def test_unauthenticated_user_returns_401_directly(self):
        factory = RequestFactory()
        url = reverse('app:update_status', kwargs={'ctype': 'movie', 'cid': self.content_id})
        request = factory.post(url, json.dumps({'status': 'completed'}), content_type='application/json')
        request.user = AnonymousUser()
        
        response = update_status.__wrapped__(request, ctype='movie', cid=self.content_id)
        self.assertEqual(response.status_code, 401)
        data = json.loads(response.content)
        self.assertEqual(data['status'], 'error')
        self.assertEqual(data['message'], 'Authentication required')
