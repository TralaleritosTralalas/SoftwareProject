from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db.models import Q
from app.models import Catalog, Notification


User = get_user_model()


class Command(BaseCommand):
    help = "Notifica a usuarios sobre contenido audiovisual no disponible en el catálogo"

    def add_arguments(self, parser):
        parser.add_argument(
            '--dry-run', action='store_true',
            help='Solo muestra lo que se notificaría sin crear notificaciones'
        )

    def handle(self, *args, **options):
        unavailable = Catalog.objects.filter(state='unavailable').select_related(
            'content', 'platform'
        )

        if not unavailable.exists():
            self.stdout.write(self.style.SUCCESS('✓ No hay contenido no disponible en el catálogo'))
            return

        self.stdout.write(self.style.WARNING(
            f'\n--- Contenido no disponible: {unavailable.count()} registros ---\n'
        ))

        total_notifications = 0

        for entry in unavailable:
            content = entry.content
            platform = entry.platform
            title = content.title
            msg = f"'{title}' is no longer available on {platform.platform_name}"

            affected = User.objects.filter(
                Q(favorite__content=content) |
                Q(watchlist__content=content) |
                Q(visualizationprogress__content=content)
            ).distinct()

            if not affected.exists():
                self.stdout.write(f'  - "{title}": 0 usuarios afectados (omitido)')
                continue

            if options['dry_run']:
                self.stdout.write(
                    f'  ✗ "{title}" ({content._meta.model_name}) → '
                    f'{affected.count()} usuarios afectados [DRY-RUN]'
                )
                total_notifications += affected.count()
                continue

            created_count = 0
            for user in affected:
                notification, created = Notification.objects.get_or_create(
                    user=user,
                    message=msg,
                    defaults={'seen': False}
                )
                if created:
                    created_count += 1

            total_notifications += created_count
            self.stdout.write(
                f'  ✗ "{title}" ({content._meta.model_name}) → '
                f'{created_count} notificaciones creadas'
            )

        self.stdout.write(self.style.SUCCESS(
            f'\n✓ Proceso completado: {total_notifications} notificaciones generadas'
        ))
