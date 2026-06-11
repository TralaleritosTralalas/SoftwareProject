from django.urls import reverse
from app.tests.base import BaseTestSuite
from app.models import Watchlist, User
import json


class WatchlistCRUDTest(BaseTestSuite):
    def setUp(self):
        super().setUp()
        self.watchlist = Watchlist.objects.create(user=self.user, name="My List")
        self.client.login(username='tester', password=self.user_pwd)

    def test_get_user_lists(self):
        url = reverse('app:get_user_lists')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue(data['success'])
        self.assertEqual(len(data['lists']), 1)
        self.assertEqual(data['lists'][0]['name'], "My List")

    def test_create_list_success(self):
        url = reverse('app:create_list')
        response = self.client.post(
            url,
            json.dumps({'name': 'New Watchlist'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue(data['success'])
        self.assertEqual(data['list']['name'], 'New Watchlist')
        self.assertTrue(Watchlist.objects.filter(user=self.user, name='New Watchlist').exists())

    def test_create_list_validation_empty_name(self):
        url = reverse('app:create_list')
        response = self.client.post(
            url,
            json.dumps({'name': '  '}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertFalse(data['success'])
        self.assertEqual(data['error'], 'List name is required')

    def test_rename_list_success(self):
        url = reverse('app:rename_list', kwargs={'list_id': self.watchlist.id})
        response = self.client.put(
            url,
            json.dumps({'name': 'Renamed List'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue(data['success'])
        self.watchlist.refresh_from_db()
        self.assertEqual(self.watchlist.name, 'Renamed List')

    def test_rename_list_duplicate_name_constraint(self):
        Watchlist.objects.create(user=self.user, name="Other List")
        url = reverse('app:rename_list', kwargs={'list_id': self.watchlist.id})
        response = self.client.put(
            url,
            json.dumps({'name': 'Other List'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertFalse(data['success'])
        self.assertEqual(data['error'], 'A list with this name already exists')

    def test_delete_list_success(self):
        url = reverse('app:delete_list', kwargs={'list_id': self.watchlist.id})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue(data['success'])
        self.assertFalse(Watchlist.objects.filter(id=self.watchlist.id).exists())

    def test_multi_tenancy_authorization_enforcement(self):
        # Create user B
        user_b = User.objects.create_user(username='tester_b', email='b@test.com', password=self.user_pwd)
        self.client.login(username='tester_b', password=self.user_pwd)

        # Try to rename User A's list
        url_rename = reverse('app:rename_list', kwargs={'list_id': self.watchlist.id})
        response = self.client.put(
            url_rename,
            json.dumps({'name': 'Hacked'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertFalse(data['success'])
        self.assertEqual(data['error'], 'List not found')

        # Try to delete User A's list
        url_delete = reverse('app:delete_list', kwargs={'list_id': self.watchlist.id})
        response = self.client.post(url_delete)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertFalse(data['success'])
        self.assertEqual(data['error'], 'List not found')
        
        self.assertTrue(Watchlist.objects.filter(id=self.watchlist.id).exists())
