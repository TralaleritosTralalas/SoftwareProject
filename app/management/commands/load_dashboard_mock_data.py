import random
from datetime import date, timedelta
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from app.models import (
    User, Country, Genre, Director, AgeRating, Language,
    Platform, Movie, Series, Catalog, Statistics, Favorite,
    VisualizationProgress, Watchlist, Notification, AudiovisualContent
)

class Command(BaseCommand):
    help = 'Populates the database with large mock data for dashboard analytics'

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Clear all existing mock data before loading',
        )

    def handle(self, *args, **options):
        if options['clear']:
            self.stdout.write(self.style.WARNING("Clearing existing database contents (preserving superusers)..."))
            Statistics.objects.all().delete()
            Catalog.objects.all().delete()
            VisualizationProgress.objects.all().delete()
            Favorite.objects.all().delete()
            Watchlist.objects.all().delete()
            Notification.objects.all().delete()
            Movie.objects.all().delete()
            Series.objects.all().delete()
            AudiovisualContent.objects.all().delete()
            Platform.objects.all().delete()
            User.objects.filter(is_superuser=False).delete()
            Director.objects.all().delete()
            Genre.objects.all().delete()
            Country.objects.all().delete()
            Language.objects.all().delete()
            AgeRating.objects.all().delete()
            self.stdout.write(self.style.SUCCESS("Database cleared successfully."))

        self.stdout.write("Generating mock data...")

        manager_group, _ = Group.objects.get_or_create(name='manager')
        director_group, _ = Group.objects.get_or_create(name='director')
        technical_group, _ = Group.objects.get_or_create(name='technical')

        genres_data = [
            ("Action", "Exciting action movies and thrillers"),
            ("Comedy", "Funny movies and sitcoms"),
            ("Drama", "Emotional and deep character stories"),
            ("Sci-Fi", "Science fiction, space, and technology"),
            ("Romance", "Love stories and romantic comedies"),
            ("Horror", "Scary movies and horror series"),
            ("Thriller", "Suspenseful and mysterious plots"),
            ("Documentary", "Real-world stories and educational features"),
            ("Anime", "Japanese animation style films and series"),
        ]
        genres = []
        for name, desc in genres_data:
            g, _ = Genre.objects.get_or_create(name=name, defaults={'description': desc})
            genres.append(g)

        countries_data = [
            ("United States", "US"),
            ("United Kingdom", "GB"),
            ("Spain", "ES"),
            ("Japan", "JP"),
            ("France", "FR"),
            ("South Korea", "KR"),
            ("Canada", "CA"),
        ]
        countries = []
        for name, iso in countries_data:
            c, _ = Country.objects.get_or_create(name=name, defaults={'iso_code': iso})
            countries.append(c)

        languages_data = [
            ("English", "en"),
            ("Spanish", "es"),
            ("Japanese", "ja"),
            ("French", "fr"),
            ("Korean", "ko"),
        ]
        languages = []
        for name, iso in languages_data:
            l, _ = Language.objects.get_or_create(name=name, defaults={'iso_code': iso})
            languages.append(l)

        age_ratings_data = [
            ("All Audiences", 0),
            ("Recommended for children over 7", 7),
            ("Recommended for children over 12", 12),
            ("Not recommended for under 16", 16),
            ("Not recommended for under 18", 18),
        ]
        age_ratings = []
        for desc, min_age in age_ratings_data:
            ar, _ = AgeRating.objects.get_or_create(minimum_age=min_age, defaults={'description': desc})
            age_ratings.append(ar)

        directors_data = [
            ("Christopher Nolan", date(1970, 7, 30), "United States"),
            ("Steven Spielberg", date(1946, 12, 18), "United States"),
            ("Quentin Tarantino", date(1963, 3, 27), "United States"),
            ("Hayao Miyazaki", date(1941, 1, 5), "Japan"),
            ("Bong Joon Ho", date(1969, 9, 14), "South Korea"),
            ("Denis Villeneuve", date(1967, 10, 3), "Canada"),
            ("Pedro Almodóvar", date(1949, 9, 25), "Spain"),
            ("Martin Scorsese", date(1942, 11, 17), "United States"),
            ("Guillermo del Toro", date(1964, 10, 9), "United States"),
            ("Ridley Scott", date(1937, 11, 30), "United Kingdom"),
        ]
        directors = []
        for name, dob, c_name in directors_data:
            country_obj = Country.objects.filter(name=c_name).first()
            d, _ = Director.objects.get_or_create(name=name, defaults={'birth_date': dob, 'country': country_obj})
            directors.append(d)

        platforms = []
        for i in [1, 2, 3]:
            username = f"manager{i}"
            m = User.objects.filter(username=username).first()
            if not m:
                m = User.objects.create_user(
                    username=username,
                    email=f"manager{i}@platform.com",
                    password="password123",
                    first_name=f"Manager",
                    last_name=f"Platform {i}",
                    role=manager_group
                )
            else:
                m.role = manager_group
                m.save()

            p, _ = Platform.objects.get_or_create(
                platform_name=f"Platform {i}",
                defaults={
                    'url_api': f"https://api.platform{i}.com/v1",
                    'p_manager': m
                }
            )
            platforms.append(p)

        director_user = User.objects.filter(username="director").first()
        if not director_user:
            director_user = User.objects.create_user(
                username="director",
                email="director@company.com",
                password="password123",
                first_name="General",
                last_name="Director",
                role=director_group
            )
        else:
            director_user.role = director_group
            director_user.save()

        regular_users = []
        for i in range(1, 21):
            username = f"user{i}"
            u = User.objects.filter(username=username).first()
            if not u:
                u = User.objects.create_user(
                    username=username,
                    email=f"user{i}@example.com",
                    password="password123",
                    first_name=f"User {i}",
                    last_name="Tester",
                    gender=random.choice(['male', 'female', 'non-binary', 'other']),
                    birth_date=date(random.randint(1980, 2010), random.randint(1, 12), random.randint(1, 28)),
                    country=random.choice(countries)
                )
                u.favorite_genres.add(*random.sample(genres, k=random.randint(1, 3)))
                u.save()
            regular_users.append(u)

        movies_titles = [
            ("Inception", "A thief who steals corporate secrets through dream-sharing is given the task of planting an idea.", 8.8, "Christopher Nolan"),
            ("Interstellar", "Explorers travel through a wormhole in search of a new home for humanity.", 8.7, "Christopher Nolan"),
            ("Dunkirk", "Allied soldiers are evacuated during a fierce battle in World War II.", 7.8, "Christopher Nolan"),
            ("Jurassic Park", "A theme park on an island fails, letting dinosaurs run wild.", 8.2, "Steven Spielberg"),
            ("Schindler's List", "Industrialist Oskar Schindler saves Jewish workers in occupied Poland.", 9.0, "Steven Spielberg"),
            ("Saving Private Ryan", "Soldiers go behind enemy lines to retrieve a paratrooper.", 8.6, "Steven Spielberg"),
            ("Pulp Fiction", "The lives of mob hitmen, a boxer, a gangster's wife, and bandits intertwine.", 8.9, "Quentin Tarantino"),
            ("Django Unchained", "A freed slave sets out to rescue his wife from a brutal plantation owner.", 8.4, "Quentin Tarantino"),
            ("Kill Bill: Vol. 1", "A former assassin wreaks vengeance on the team that betrayed her.", 8.2, "Quentin Tarantino"),
            ("Spirited Away", "A girl wanders into a world ruled by gods, witches, and spirits.", 8.6, "Hayao Miyazaki"),
            ("My Neighbor Totoro", "Two girls have adventures with forest spirits in the country.", 8.1, "Hayao Miyazaki"),
            ("Princess Mononoke", "A young warrior is caught in a war between forest gods and humans.", 8.4, "Hayao Miyazaki"),
            ("Parasite", "Greed and class discrimination threaten a newly formed relationship between two families.", 8.5, "Bong Joon Ho"),
            ("Snowpiercer", "Survivors of a climate experiment live aboard a train divided by class.", 7.1, "Bong Joon Ho"),
            ("Incendies", "Twins journey to the Middle East to fulfill their mother's last wishes.", 8.3, "Denis Villeneuve"),
            ("Arrival", "A linguist works to communicate with alien spacecraft appearing on Earth.", 7.9, "Denis Villeneuve"),
            ("Dune", "A noble family becomes embroiled in a war for control of the galaxy's spice.", 8.0, "Denis Villeneuve"),
            ("The Skin I Live In", "A plastic surgeon creates a type of synthetic skin that resists damage.", 7.6, "Pedro Almodóvar"),
            ("Volver", "A mother returns to her home town as a ghost to fix unresolved problems.", 7.6, "Pedro Almodóvar"),
            ("Goodfellas", "A young man grows up in the mob and works to stay on top.", 8.7, "Martin Scorsese"),
            ("The Departed", "An undercover cop and a mole in the police attempt to identify each other.", 8.5, "Martin Scorsese"),
            ("Pan's Labyrinth", "A girl escapes into a dark but captivating fantasy world during WWII Spain.", 8.2, "Guillermo del Toro"),
            ("Blade Runner", "A detective is tasked with hunting down four rogue replicants on Earth.", 8.1, "Ridley Scott"),
            ("Gladiator", "A general sets out to exact vengeance against the corrupt emperor.", 8.5, "Ridley Scott"),
            ("Alien", "A commercial spacecraft crew encounters a deadly, parasitic lifeform.", 8.5, "Ridley Scott"),
            ("The Dark Knight", "Batman accepts his greatest psychological test against the Joker.", 9.0, "Christopher Nolan"),
            ("Catch Me If You Can", "An FBI agent pursues a brilliant young check-forger.", 8.1, "Steven Spielberg"),
            ("The Wolf of Wall Street", "A stockbroker lives the high life of greed and corruption.", 8.2, "Martin Scorsese"),
            ("Inglourious Basterds", "Jewish U.S. soldiers plan to assassinate Nazi leaders in WWII France.", 8.3, "Quentin Tarantino"),
            ("Blade Runner 2049", "A new blade runner unearths a secret that could plunge society into chaos.", 8.0, "Denis Villeneuve"),
        ]
        
        movies = []
        for title, syn, rating, dir_name in movies_titles:
            dir_obj = Director.objects.filter(name=dir_name).first() or random.choice(directors)
            g = random.choice(genres)
            c = random.choice(countries)
            l = random.choice(languages)
            ar = random.choice(age_ratings)
            
            m, _ = Movie.objects.get_or_create(
                title=title,
                defaults={
                    'synopsis': syn,
                    'rating': rating,
                    'genre': g,
                    'director': dir_obj,
                    'country': c,
                    'language': l,
                    'age_rating': ar,
                    'year': random.randint(1990, 2024),
                    'release_date': date(random.randint(1990, 2024), random.randint(1, 12), random.randint(1, 28)),
                    'duration_minutes': random.randint(80, 180),
                }
            )
            movies.append(m)

        series_titles = [
            ("Breaking Bad", "A chemistry teacher manufactures methamphetamine to secure his family's future.", 9.5, "Martin Scorsese"),
            ("Stranger Things", "A small town uncovers a mystery involving supernatural forces and secret experiments.", 8.7, "Steven Spielberg"),
            ("Game of Thrones", "Noble families fight for control of the Iron Throne.", 9.2, "Ridley Scott"),
            ("Chernobyl", "A dramatization of the 1986 nuclear disaster in the USSR.", 9.4, "Denis Villeneuve"),
            ("The Crown", "Follows the political rivalries and romance of Queen Elizabeth II's reign.", 8.6, "Ridley Scott"),
            ("Dark", "A family saga with a time-travel twist set in a German town.", 8.7, "Christopher Nolan"),
            ("Succession", "A media tycoon's children fight for control of the family empire.", 8.8, "Martin Scorsese"),
            ("Mindhunter", "FBI agents delve into the psychology of serial killers.", 8.6, "Christopher Nolan"),
            ("True Detective", "Anthology series following police investigations that unearth dark secrets.", 8.9, "Quentin Tarantino"),
            ("Peaky Blinders", "A gangster family epic set in 1900s Birmingham.", 8.8, "Ridley Scott"),
            ("Sherlock", "A modern update of Sherlock Holmes solving crimes in London.", 9.1, "Steven Spielberg"),
            ("Black Mirror", "An anthology series exploring humanity's dark relationship with technology.", 8.7, "Denis Villeneuve"),
            ("The Boys", "Vigilantes set out to take down corrupt superheroes.", 8.7, "Quentin Tarantino"),
            ("The Queen's Gambit", "An orphaned chess prodigy rises to the top while fighting addiction.", 8.6, "Pedro Almodóvar"),
            ("Better Call Saul", "Follows the trials of criminal lawyer Jimmy McGill before Breaking Bad.", 8.9, "Martin Scorsese"),
            ("Narcos", "A chronicled look at the rise and fall of drug kingpins.", 8.8, "Bong Joon Ho"),
            ("Fleabag", "A dry-witted woman navigates life and love in London.", 8.7, "Pedro Almodóvar"),
            ("Attack on Titan", "A young man vows to cleanse the earth of giant humanoid Titans.", 9.0, "Hayao Miyazaki"),
        ]

        series_list = []
        for title, syn, rating, dir_name in series_titles:
            dir_obj = Director.objects.filter(name=dir_name).first() or random.choice(directors)
            g = random.choice(genres)
            c = random.choice(countries)
            l = random.choice(languages)
            ar = random.choice(age_ratings)
            
            start_y = random.randint(2000, 2020)
            s, _ = Series.objects.get_or_create(
                title=title,
                defaults={
                    'synopsis': syn,
                    'rating': rating,
                    'genre': g,
                    'director': dir_obj,
                    'country': c,
                    'language': l,
                    'age_rating': ar,
                    'start_year': start_y,
                    'end_year': start_y + random.randint(1, 8) if random.choice([True, False]) else None,
                    'total_seasons': random.randint(1, 10),
                }
            )
            series_list.append(s)

        all_content = movies + series_list

        for c in all_content:
            assigned_platforms = random.sample(platforms, k=random.randint(1, len(platforms)))
            for p in assigned_platforms:
                Catalog.objects.get_or_create(
                    platform=p,
                    content=c,
                    defaults={'state': random.choice(['available', 'available', 'available', 'coming_soon'])}
                )

        today = date.today()
        weeks = [today - timedelta(days=today.weekday() + (i * 7)) for i in range(12)]

        for p in platforms:
            base_clicks = random.randint(1000, 5000)
            base_favs = random.randint(100, 500)
            for w in weeks:
                clicks = base_clicks + random.randint(-400, 800)
                favs = base_favs + random.randint(-40, 80)
                
                clicks = max(clicks, 0)
                favs = max(favs, 0)
                
                Statistics.objects.get_or_create(
                    platform=p,
                    week=w,
                    defaults={
                        'total_clicks': clicks,
                        'total_favorites': favs
                    }
                )

        for u in regular_users:
            chosen_contents = random.sample(all_content, k=random.randint(5, 10))
            for c in chosen_contents:
                if random.choice([True, False]):
                    Favorite.objects.get_or_create(user=u, content=c)

                completed = random.choice([True, False])
                last_min = random.randint(10, 120) if not completed else 120
                VisualizationProgress.objects.get_or_create(
                    user=u,
                    content=c,
                    defaults={
                        'last_minute': last_min,
                        'completed': completed
                    }
                )

        self.stdout.write(self.style.SUCCESS(f"Successfully loaded mock data:"))
        self.stdout.write(self.style.SUCCESS(f" - {len(platforms)} Platforms (Platform 1, 2, 3)"))
        self.stdout.write(self.style.SUCCESS(f" - {len(movies)} Movies"))
        self.stdout.write(self.style.SUCCESS(f" - {len(series_list)} Series"))
        self.stdout.write(self.style.SUCCESS(f" - 12 weeks of weekly click/favorite statistics"))
        self.stdout.write(self.style.SUCCESS(f" - User favorites & progress histories"))
