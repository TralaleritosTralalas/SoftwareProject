from django.urls import reverse
from app.tests.base import BaseTestSuite
from app.models import Notification
from app.context_processors import unread_notifications
from django.test import RequestFactory
import json


class NotificationsTest(BaseTestSuite):
    def setUp(self):
        super().setUp()
        self.client.login(username='tester', password=self.user_pwd)
        self.n1 = Notification.objects.create(user=self.user, message="Update 1", seen=False)
        self.n2 = Notification.objects.create(user=self.user, message="Update 2", seen=False)

    def test_unread_notifications_context_processor(self):
        # Directly test the context processor
        factory = RequestFactory()
        request = factory.get(reverse('app:main'))
        request.user = self.user

        context = unread_notifications(request)
        self.assertEqual(context['unread_count'], 2)
        self.assertEqual(list(context['unread_notifications']), [self.n2, self.n1])

    def test_unread_notifications_context_processor_anonymous(self):
        from django.contrib.auth.models import AnonymousUser
        factory = RequestFactory()
        request = factory.get(reverse('app:main'))
        request.user = AnonymousUser()

        context = unread_notifications(request)
        self.assertEqual(context, {})

    def test_mark_single_notification_seen(self):
        url = reverse('app:mark_notification_seen')
        response = self.client.post(
            url,
            json.dumps({'id': self.n1.id}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content)['count'], 1)

        self.n1.refresh_from_db()
        self.assertTrue(self.n1.seen)
        self.n2.refresh_from_db()
        self.assertFalse(self.n2.seen)

    def test_mark_all_notifications_seen(self):
        url = reverse('app:mark_notification_seen')
        response = self.client.post(
            url,
            json.dumps({'all': True}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content)['count'], 0)

        self.n1.refresh_from_db()
        self.assertTrue(self.n1.seen)
        self.n2.refresh_from_db()
        self.assertTrue(self.n2.seen)
