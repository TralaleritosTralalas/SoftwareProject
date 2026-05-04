from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date


class User(AbstractUser):
    ROLE_CHOICES = [
        ('normal', 'Normal'),
        ('manager', 'Platform Manager'),
        ('tech', 'Technical Manager'),
        ('director', 'Direction'),
        ('admin', 'Administrator'),
    ]
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('non-binary', 'Non-binary'),
        ('other', 'Other'),
    ]
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, default='normal')
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True, verbose_name="Fecha de Nacimiento")
    country = models.ForeignKey('Country', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="País")
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True, verbose_name="Foto de Perfil")
    onboarding_completed = models.BooleanField(default=False)
    favorite_genres = models.ManyToManyField('Genre', blank=True, related_name='users')

    @property
    def age(self):
        if not self.birth_date:
            return None

        today = date.today()

        return today.year - self.birth_date.year - (
                    (today.month, today.day) < (self.birth_date.month, self.birth_date.day))

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"


class Country(models.Model):
    name = models.CharField(max_length=100)
    iso_code = models.CharField(max_length=5)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=200)
    birth_date = models.DateField()
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class AgeRating(models.Model):
    description = models.CharField(max_length=100)
    minimum_age = models.IntegerField()

    def __str__(self):
        return f"+{self.minimum_age} - {self.description}"


class Language(models.Model):
    name = models.CharField(max_length=100)
    iso_code = models.CharField(max_length=5)

    def __str__(self):
        return self.name


class AudiovisualContent(models.Model):
    title = models.CharField(max_length=200)
    synopsis = models.TextField()
    rating = models.FloatField(default=0.0)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)
    age_rating = models.ForeignKey(AgeRating, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Movie(AudiovisualContent):
    year = models.IntegerField()
    release_date = models.DateField()
    duration_minutes = models.IntegerField()


class Series(AudiovisualContent):
    start_year = models.IntegerField()
    end_year = models.IntegerField(null=True, blank=True)
    total_seasons = models.IntegerField()


class Platform(models.Model):
    platform_name = models.CharField(max_length=100)
    url_api = models.URLField()
    p_manager = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'manager'})

    def __str__(self):
        return self.platform_name


class Catalog(models.Model):
    STATE_CHOICES = [
        ('available', 'Available'),
        ('unavailable', 'Unavailable'),
        ('coming_soon', 'Coming Soon'),
    ]
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    content = models.ForeignKey(AudiovisualContent, on_delete=models.CASCADE)
    state = models.CharField(max_length=20, choices=STATE_CHOICES, default='available')

    def __str__(self):
        return f"{self.platform.platform_name} - {self.content.title}"


class Statistics(models.Model):
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    total_favorites = models.IntegerField(default=0)
    total_clicks = models.IntegerField(default=0)
    week = models.DateField()

    def __str__(self):
        return f"Stats for {self.platform} - Week: {self.week}"


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    seen = models.BooleanField(default=False)

    def __str__(self):
        return f"To: {self.user.username} - Seen: {self.seen}"


class VisualizationProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.ForeignKey(AudiovisualContent, on_delete=models.CASCADE)
    last_minute = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} watching {self.content.title} (Min: {self.last_minute})"


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.ForeignKey(AudiovisualContent, on_delete=models.CASCADE)


class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.ForeignKey(AudiovisualContent, on_delete=models.CASCADE)