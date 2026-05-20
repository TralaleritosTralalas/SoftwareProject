from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta
from app.models import AudiovisualContent, Notification


User = get_user_model()


class Command(BaseCommand):
    help = "Notifica a usuarios sobre contenido nuevo que coincide con sus géneros favoritos"

    def add_arguments(self, parser):
        parser.add_argument(
            '--hours', type=int, default=24,
            help='Ventana de horas hacia atrás para buscar contenido nuevo'
        )
        parser.add_argument(
            '--dry-run', action='store_true',
            help='Solo muestra lo que se notificaría sin crear notificaciones'
        )

    def handle(self, *args, **options):
        since = timezone.now() - timedelta(hours=options['hours'])

        recent = AudiovisualContent.objects.filter(
            created_at__gte=since, genre__isnull=False
        ).select_related('genre')

        if not recent.exists():
            self.stdout.write(self.style.SUCCESS('✓ No hay contenido nuevo en las últimas %d horas' % options['hours']))
            return

        self.stdout.write(self.style.WARNING(
            '\n--- Contenido nuevo (últimas %d horas): %d ---\n' % (options['hours'], recent.count())
        ))

        total_notifications = 0

        for content in recent:
            genre = content.genre
            users = User.objects.filter(favorite_genres=genre)

            if not users.exists():
                self.stdout.write('  - "%s" (%s): 0 usuarios (omitido)' % (content.title, genre.name))
                continue

            if options['dry_run']:
                self.stdout.write(
                    '  ✓ "%s" (%s) -> %d usuarios [DRY-RUN]'
                    % (content.title, genre.name, users.count())
                )
                total_notifications += users.count()
                continue

            created_count = 0
            for user in users:
                msg = "'%s' - New content matching your favorite genres" % content.title
                notification, created = Notification.objects.get_or_create(
                    user=user,
                    message=msg,
                    defaults={'seen': False}
                )
                if created:
                    created_count += 1

            total_notifications += created_count
            self.stdout.write(
                '  ✓ "%s" (%s) -> %d notificaciones creadas'
                % (content.title, genre.name, created_count)
            )

        self.stdout.write(self.style.SUCCESS(
            '\n✓ Proceso completado: %d notificaciones generadas' % total_notifications
        ))
