import requests
import logging
from django.core.management.base import BaseCommand
from django.db import transaction
from django.contrib.auth import get_user_model
from app.models import (
    Genre, Director, AgeRating,
    Movie, Series, Platform, Catalog
)
from decouple import config

logger = logging.getLogger(__name__)


def parse_date(value):
    """Convert '1963-03-27T00:00:00.000Z' or '1963-03-27' to 'YYYY-MM-DD'. Returns None if invalid."""
    if not value:
        return None
    return str(value)[:10]


class Command(BaseCommand):
    help = 'Importa contenido audiovisual desde las APIs de JoinProject'

    API_CONFIG = {
        'https://joinproject-api1.safont.dev': (config('API_KEY_LOCAL_1'), 'Platform 1'),
        'https://joinproject-api2.safont.dev': (config('API_KEY_LOCAL_2'), 'Platform 2'),
        'https://joinproject-api3.safont.dev': (config('API_KEY_LOCAL_3'), 'Platform 3'),
    }

    RESOURCES = ['genres', 'age-ratings', 'directors', 'movies', 'series']

    def add_arguments(self, parser):
        parser.add_argument('--api', type=int, choices=[1, 2, 3], help='API específica (1, 2 o 3)')
        parser.add_argument('--clear', action='store_true', help='Limpiar DB antes de importar')

    def handle(self, *args, **options):
        if options['clear']:
            self.clear_data()

        target_apis = list(self.API_CONFIG.items())
        if options['api']:
            url = list(self.API_CONFIG.keys())[options['api'] - 1]
            target_apis = [(url, self.API_CONFIG[url])]

        for base_url, (key, platform_name) in target_apis:
            self.stdout.write(self.style.WARNING(f'\n--- Importando desde: {platform_name} ({base_url}) ---'))
            for resource in self.RESOURCES:
                self.fetch_and_process(base_url, key, resource, platform_name)

    def fetch_and_process(self, base_url, key, resource, platform_name):
        url = f"{base_url.rstrip('/')}/{resource}"
        headers = {'X-API-KEY': key, 'Accept': 'application/json'}
        try:
            response = requests.get(url, headers=headers, timeout=15)
            if response.status_code == 200:
                self.process_resource(resource, response.json(), base_url, platform_name)
                self.stdout.write(self.style.SUCCESS(f'  ✓ {resource} importado correctamente.'))
            else:
                self.stdout.write(self.style.ERROR(f'  ✗ Error {response.status_code} en {url}'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'  ✗ Fallo de red en {resource}: {e}'))

    @transaction.atomic
    def process_resource(self, r_type, data, base_url, platform_name):
        if r_type == 'genres':
            for item in data:
                Genre.objects.get_or_create(
                    name=item['name'],
                    defaults={'description': item.get('description', '')}
                )

        elif r_type == 'age-ratings':
            for item in data:
                AgeRating.objects.get_or_create(
                    description=item['description'],
                    defaults={'minimum_age': item.get('minimum_age') or 0}
                )

        elif r_type == 'directors':
            for item in data:
                birth_date = parse_date(item.get('birth_date')) or '1900-01-01'
                Director.objects.get_or_create(
                    name=item['name'],
                    defaults={'birth_date': birth_date}
                )

        elif r_type == 'movies':
            platform = self._get_or_create_platform(base_url, platform_name)
            for item in data:
                try:
                    # FIX: Use the *_id fields to look up related objects
                    genre = None
                    if item.get('genre_id'):
                        # Find genre by the API id - we need to map it
                        # Since we imported genres first, we can find by index or create a mapping
                        genre = Genre.objects.all()[item['genre_id'] - 1] if item['genre_id'] <= Genre.objects.count() else None
                    
                    director = None
                    if item.get('director_id'):
                        director = Director.objects.all()[item['director_id'] - 1] if item['director_id'] <= Director.objects.count() else None
                    
                    age_rating = None
                    if item.get('age_rating_id'):
                        age_rating = AgeRating.objects.all()[item['age_rating_id'] - 1] if item['age_rating_id'] <= AgeRating.objects.count() else None
                    
                    movie, _ = Movie.objects.update_or_create(
                        title=item['title'],
                        defaults={
                            'synopsis': item.get('synopsis') or '',
                            'rating': float(item.get('rating') or 0),  # Convert string to float
                            'year': item.get('year') or 2000,
                            'release_date': parse_date(item.get('release_date')) or '2000-01-01',
                            'duration_minutes': item.get('duration_minutes') or 90,  # Default duration
                            'genre': genre,
                            'director': director,
                            'age_rating': age_rating,
                        }
                    )
                    Catalog.objects.get_or_create(
                        platform=platform, 
                        content=movie,
                        defaults={'state': 'available'}
                    )
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f'    ! Error guardando película "{item.get("title")}": {e}'))

        elif r_type == 'series':
            platform = self._get_or_create_platform(base_url, platform_name)
            for item in data:
                try:
                    # FIX: Use the *_id fields to look up related objects
                    genre = None
                    if item.get('genre_id'):
                        genre = Genre.objects.all()[item['genre_id'] - 1] if item['genre_id'] <= Genre.objects.count() else None
                    
                    director = None
                    if item.get('director_id'):
                        director = Director.objects.all()[item['director_id'] - 1] if item['director_id'] <= Director.objects.count() else None
                    
                    serie, _ = Series.objects.update_or_create(
                        title=item['title'],
                        defaults={
                            'synopsis': item.get('synopsis') or '',
                            'rating': float(item.get('rating') or 0),  # Convert string to float
                            'start_year': item.get('start_year') or 2000,
                            'end_year': item.get('end_year'),
                            'total_seasons': item.get('total_seasons') or 1,
                            'genre': genre,
                            'director': director,
                        }
                    )
                    Catalog.objects.get_or_create(
                        platform=platform, 
                        content=serie,
                        defaults={'state': 'available'}
                    )
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f'    ! Error guardando serie "{item.get("title")}": {e}'))

    def _get_or_create_platform(self, base_url, platform_name):
        User = get_user_model()
        manager = User.objects.filter(is_superuser=True).first()
        platform, _ = Platform.objects.get_or_create(
            platform_name=platform_name,
            defaults={'url_api': base_url, 'p_manager': manager}
        )
        return platform

    def clear_data(self):
        self.stdout.write(self.style.WARNING('Limpiando base de datos...'))
        Catalog.objects.all().delete()
        Movie.objects.all().delete()
        Series.objects.all().delete()
        Director.objects.all().delete()
        AgeRating.objects.all().delete()
        Genre.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Base de datos limpia.'))