import requests
import logging
from django.core.management.base import BaseCommand
from app.models import Movie, Series
from decouple import config
from time import sleep

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Fetch poster and backdrop image URLs from TMDB API'

    TMDB_API_KEY = config('TMDB_API_KEY', default='')
    TMDB_BASE_URL = 'https://api.themoviedb.org/3'
    TMDB_IMAGE_BASE_URL = 'https://image.tmdb.org/t/p/w500'
    TMDB_BACKDROP_BASE_URL = 'https://image.tmdb.org/t/p/w1280'

    def add_arguments(self, parser):
        parser.add_argument('--type', type=str, choices=['movie', 'series', 'all'], default='all', help='Content type to fetch images for')
        parser.add_argument('--limit', type=int, help='Limit number of items to process')
        parser.add_argument('--force', action='store_true', help='Force re-fetch even if URLs exist')

    def handle(self, *args, **options):
        if not self.TMDB_API_KEY:
            self.stdout.write(self.style.ERROR('TMDB_API_KEY not found in environment variables!'))
            return

        content_type = options['type']
        limit = options.get('limit')
        force = options['force']

        if content_type in ['movie', 'all']:
            self.fetch_movie_images(limit=limit, force=force)
        
        if content_type in ['series', 'all']:
            self.fetch_series_images(limit=limit, force=force)

    def fetch_movie_images(self, limit=None, force=False):
        self.stdout.write(self.style.WARNING('\n--- Fetching Movie Image URLs from TMDB ---'))
        
        movies = Movie.objects.all()
        if not force:
            movies = movies.filter(poster_url__isnull=True) | movies.filter(poster_url='')
        
        if limit:
            movies = movies[:limit]
        
        total = movies.count()
        success_count = 0
        
        for idx, movie in enumerate(movies, 1):
            self.stdout.write(f'Processing {idx}/{total}: {movie.title} ({movie.year})')
            
            try:
                search_url = f'{self.TMDB_BASE_URL}/search/movie'
                params = {
                    'api_key': self.TMDB_API_KEY,
                    'query': movie.title,
                    'year': movie.year
                }
                
                response = requests.get(search_url, params=params, timeout=10)
                
                if response.status_code == 200:
                    results = response.json().get('results', [])
                    
                    if results:
                        tmdb_movie = results[0]
                        
                        if tmdb_movie.get('poster_path'):
                            movie.poster_url = f"{self.TMDB_IMAGE_BASE_URL}{tmdb_movie['poster_path']}"
                        
                        if tmdb_movie.get('backdrop_path'):
                            movie.backdrop_url = f"{self.TMDB_BACKDROP_BASE_URL}{tmdb_movie['backdrop_path']}"
                        
                        movie.save()
                        success_count += 1
                        self.stdout.write(self.style.SUCCESS(f'  ✓ URLs saved for {movie.title}'))
                    else:
                        self.stdout.write(self.style.WARNING(f'  ! No TMDB results for {movie.title}'))
                else:
                    self.stdout.write(self.style.ERROR(f'  ✗ TMDB API error {response.status_code}'))
                
                sleep(0.25)
                
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'  ✗ Error processing {movie.title}: {e}'))
        
        self.stdout.write(self.style.SUCCESS(f'\nMovies processed: {success_count}/{total}'))

    def fetch_series_images(self, limit=None, force=False):
        self.stdout.write(self.style.WARNING('\n--- Fetching Series Image URLs from TMDB ---'))
        
        series = Series.objects.all()
        if not force:
            series = series.filter(poster_url__isnull=True) | series.filter(poster_url='')
        
        if limit:
            series = series[:limit]
        
        total = series.count()
        success_count = 0
        
        for idx, serie in enumerate(series, 1):
            self.stdout.write(f'Processing {idx}/{total}: {serie.title} ({serie.start_year})')
            
            try:
                search_url = f'{self.TMDB_BASE_URL}/search/tv'
                params = {
                    'api_key': self.TMDB_API_KEY,
                    'query': serie.title,
                    'first_air_date_year': serie.start_year
                }
                
                response = requests.get(search_url, params=params, timeout=10)
                
                if response.status_code == 200:
                    results = response.json().get('results', [])
                    
                    if results:
                        tmdb_serie = results[0]
                        
                        if tmdb_serie.get('poster_path'):
                            serie.poster_url = f"{self.TMDB_IMAGE_BASE_URL}{tmdb_serie['poster_path']}"
                        
                        if tmdb_serie.get('backdrop_path'):
                            serie.backdrop_url = f"{self.TMDB_BACKDROP_BASE_URL}{tmdb_serie['backdrop_path']}"
                        
                        serie.save()
                        success_count += 1
                        self.stdout.write(self.style.SUCCESS(f'  ✓ URLs saved for {serie.title}'))
                    else:
                        self.stdout.write(self.style.WARNING(f'  ! No TMDB results for {serie.title}'))
                else:
                    self.stdout.write(self.style.ERROR(f'  ✗ TMDB API error {response.status_code}'))
                
                sleep(0.25)
                
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'  ✗ Error processing {serie.title}: {e}'))
        
        self.stdout.write(self.style.SUCCESS(f'\nSeries processed: {success_count}/{total}'))