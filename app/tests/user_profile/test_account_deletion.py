from django.urls import reverse
from app.tests.base import BaseTestSuite
from app.models import User, Favorite, Movie, Genre


class AccountDeletionTest(BaseTestSuite):
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
        self.favorite = Favorite.objects.create(user=self.user, content=self.movie)
        self.client.login(username='tester', password=self.user_pwd)

    def test_delete_account_success(self):
        # Verify the favorite exists first
        self.assertTrue(Favorite.objects.filter(id=self.favorite.id).exists())

        response = self.client.post(reverse('app:delete_account'))
        
        # Verify redirection to app:home
        self.assertRedirects(response, reverse('app:home'))

        # Verify user is deleted from the database
        self.assertFalse(User.objects.filter(id=self.user.id).exists())

        # Verify session is flushed (client is logged out)
        self.assertNotIn('_auth_user_id', self.client.session)

        # Verify clean cascade on Favorite (should be deleted)
        self.assertFalse(Favorite.objects.filter(id=self.favorite.id).exists())
