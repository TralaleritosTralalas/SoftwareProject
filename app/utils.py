import csv
from datetime import timedelta
from django.utils import timezone
from django.http import HttpResponse
from .models import Statistics, AudiovisualContent


class DashboardService:
    @staticmethod
    def apply_filters(params, platform=None):
        if platform:
            stats_qs = Statistics.objects.filter(platform=platform)
            content_qs = AudiovisualContent.objects.filter(catalog__platform=platform).distinct()
        else:
            stats_qs = Statistics.objects.all()
            content_qs = AudiovisualContent.objects.all()

        today = timezone.now().date()

        range_val = params.get('range')
        start_date = params.get('start_date')
        end_date = params.get('end_date')

        if range_val:
            if range_val == '24h':
                stats_qs = stats_qs.filter(week=today)
            elif range_val == '7d':
                stats_qs = stats_qs.filter(week__gte=today - timedelta(days=7))
            elif range_val == '30d':
                stats_qs = stats_qs.filter(week__gte=today - timedelta(days=30))
            elif range_val == '90d':
                stats_qs = stats_qs.filter(week__gte=today - timedelta(days=90))
            elif range_val == 'ytd':
                stats_qs = stats_qs.filter(week__year=today.year)
        elif start_date and end_date:
            stats_qs = stats_qs.filter(week__range=[start_date, end_date])

        if not platform:
            platform_id = params.get('platform')
            if platform_id and platform_id != 'all':
                stats_qs = stats_qs.filter(platform_id=platform_id)
                content_qs = content_qs.filter(catalog__platform_id=platform_id).distinct()

        genre_id = params.get('genre')
        if genre_id and genre_id != 'all':
            content_qs = content_qs.filter(genre_id=genre_id)
            stats_qs = stats_qs.filter(platform__catalog__content__genre_id=genre_id).distinct()

        country_id = params.get('country')
        if country_id and country_id != 'all':
            content_qs = content_qs.filter(country_id=country_id)
            stats_qs = stats_qs.filter(platform__catalog__content__country_id=country_id).distinct()

        return stats_qs, content_qs

    @staticmethod
    def get_csv_response(trending_content, totals, top_p):
        response = HttpResponse(content_type='text/csv')
        today = timezone.now()
        response['Content-Disposition'] = f'attachment; filename="Strategic_Report_{today.date()}.csv"'

        response.write(u'\ufeff'.encode('utf8'))
        writer = csv.writer(response, delimiter=';')

        writer.writerow(['STRATEGIC PERFORMANCE REPORT'])
        writer.writerow(['Report Date', today.strftime('%Y-%m-%d %H:%M')])
        writer.writerow(['Total Clicks', totals['clicks']])
        writer.writerow(['Total Favorites', totals['favs']])
        writer.writerow(['Top Performing Platform', top_p['platform__platform_name'] if top_p else 'N/A'])
        writer.writerow([])

        writer.writerow(['TOP 10 CONTENT PERFORMANCE DETAILS'])
        writer.writerow(['RANK', 'TITLE', 'DIRECTOR', 'GENRE', 'COUNTRY', 'INTERACTIONS (FAVS)'])

        for i, item in enumerate(trending_content, 1):
            writer.writerow([
                i,
                item.title,
                item.director.name if item.director else 'N/A',
                item.genre.name if item.genre else 'N/A',
                item.country.name if item.country else 'N/A',
                item.fav_count
            ])

        return response
