from django.urls import reverse
from app.tests.base import BaseTestSuite
from app.models import Movie, Genre, Favorite, VisualizationProgress, Watchlist


class LibraryViewTest(BaseTestSuite):
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
        self.client.login(username='tester', password=self.user_pwd)

    def test_library_view_renders_successfully(self):
        # Create a favorite
        Favorite.objects.create(user=self.user, content=self.movie)

        # Create a visualization progress (completed)
        VisualizationProgress.objects.create(user=self.user, content=self.movie, completed=True)

        # Create a custom list
        Watchlist.objects.create(user=self.user, name="My Sci-Fi Favorites")

        response = self.client.get(reverse('app:personal_library'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/personal_library.html')
        self.assertContains(response, "Inception")
        self.assertContains(response, "My Sci-Fi Favorites")

    def test_library_view_redirects_unauthenticated(self):
        self.client.logout()
        response = self.client.get(reverse('app:personal_library'))
        self.assertEqual(response.status_code, 302)
