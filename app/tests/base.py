from django.test import TestCase
from django.contrib.auth.models import Group
from app.models import Country, Genre, User


class BaseTestSuite(TestCase):
    @classmethod
    def setUp(cls):
        cls.user_pwd = "password123"
        cls.user = User.objects.create_user(
            username='tester',
            email='test@test.com',
            password=cls.user_pwd
        )