from django.test import TestCase
from django.contrib.auth.models import Group
from app.models import Country, Genre, User


class BaseTestSuite(TestCase):
    @classmethod
    def setUp(cls):
        cls.user_pwd = "password123"
        cls.user, created = User.objects.get_or_create(
            username='tester',
            defaults={'email': 'test@test.com'}
        )
        if created or not cls.user.check_password(cls.user_pwd):
            cls.user.set_password(cls.user_pwd)
            cls.user.save()