import datetime
from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.db.models import Sum, Count
from django.conf import settings
from app.models import User, Platform, Statistics, Catalog


class Command(BaseCommand):
    help = 'Sends a performance summary email to all platform managers at the beginning of each month.'

    def handle(self, *args, **options):
        today = datetime.date.today()

        first_day_this_month = today.replace(day=1)
        last_day_last_month = first_day_this_month - datetime.timedelta(days=1)
        first_day_last_month = last_day_last_month.replace(day=1)

        last_month_name = first_day_last_month.strftime('%B %Y')

        self.stdout.write(f"Initiating calculation of monthly summaries for: {last_month_name}")

        platforms = Platform.objects.all()
        for platform in platforms:

            stats_qs = Statistics.objects.filter(
                platform=platform,
                week__range=[first_day_last_month, last_day_last_month]
            )

            totals = stats_qs.aggregate(
                clicks=Sum('total_clicks'),
                favs=Sum('total_favorites')
            )
            total_clicks = totals['clicks'] or 0
            total_favorites = totals['favs'] or 0

            top_content = Catalog.objects.filter(
                platform=platform
            ).annotate(
                fav_count=Count('content__favorite')
            ).order_by('-fav_count')[:3]

            managers = User.objects.filter(
                groups__name='manager',
                platform = platform
            ).exclude(email='')

            if not managers.exists():
                self.stdout.write(f"No managers with valid emails found for platform: {platform.platform_name}")
                continue

            recipients = [m.email for m in managers]

            subject = f"Performance Summary Report - {platform.platform_name} ({last_month_name})"

            text_body = f"Hello Manager,\n\nHere is your performance summary for {platform.platform_name} covering {last_month_name}.\n\nTotal Clicks: {total_clicks}\nTotal Favorites: {total_favorites}\n\nPlease check the dashboard tool for complete data details."

            top_items_html = ""
            for idx, item in enumerate(top_content, 1):
                top_items_html += f"""
                    <tr style="border-bottom: 1px solid #1e293b;">
                        <td style="padding: 10px; font-family: monospace; color: #64748b;">#{idx}</td>
                        <td style="padding: 10px; color: #e2e8f0; font-weight: bold;">{item.content.title}</td>
                        <td style="padding: 10px; color: #3b82f6; text-align: right; font-weight: bold;">{item.fav_count}</td>
                    </tr>
                """
            if not top_items_html:
                top_items_html = "<tr><td colspan='3' style='padding:10px; color:#64748b; font-style: italic;'>No catalog tracking interactions registered this month.</td></tr>"

            html_body = f"""
            <html>
                <body style="background-color: #020617; color: #f1f5f9; font-family: sans-serif; padding: 20px;">
                    <div style="max-width: 600px; margin: 0 auto; background-color: #0f172a; border: 1px solid #1e293b; padding: 30px; border-radius: 20px;">
                        <h2 style="color: #ffffff; text-align: center; margin-bottom: 10px;">{platform.platform_name}</h2>
                        <p style="text-align: center; color: #3b82f6; font-size: 12px; font-weight: bold; letter-spacing: 2px; margin-top: 0; text-transform: uppercase;">Monthly Performance Report</p>
                        <p style="color: #94a3b8; font-size: 14px;">Hello Manager, here is the performance audit analytics ledger compiled for the duration of <strong>{last_month_name}</strong>:</p>

                        <div style="display: flex; gap: 10px; margin: 25px 0;">
                            <div style="flex: 1; background-color: #1e293b; padding: 15px; border-radius: 12px; text-align: center;">
                                <span style="font-size: 10px; color: #94a3b8; font-weight: bold; text-transform: uppercase;">Gross Platform Clicks</span>
                                <h3 style="font-size: 24px; color: #ffffff; margin: 5px 0 0 0;">{total_clicks:,}</h3>
                            </div>
                            <div style="flex: 1; background-color: #1e293b; padding: 15px; border-radius: 12px; text-align: center;">
                                <span style="font-size: 10px; color: #3b82f6; font-weight: bold; text-transform: uppercase;">Favorite Collections</span>
                                <h3 style="font-size: 24px; color: #3b82f6; margin: 5px 0 0 0;">{total_favorites:,}</h3>
                            </div>
                        </div>

                        <h4 style="color: #ffffff; margin-bottom: 10px; border-bottom: 1px solid #1e293b; padding-bottom: 5px;">🔥 Highlighted Catalog Assets This Month</h4>
                        <table style="width: 100%; text-align: left; border-collapse: collapse; margin-bottom: 20px; font-size: 13px;">
                            <thead>
                                <tr style="color: #64748b; font-size: 11px; text-transform: uppercase;">
                                    <th style="padding: 5px 10px;">Rank</th>
                                    <th style="padding: 5px 10px;">Asset Title</th>
                                    <th style="padding: 5px 10px; text-align: right;">Saves</th>
                                </tr>
                            </thead>
                            <tbody>
                                {top_items_html}
                            </tbody>
                        </table>

                        <div style="text-align: center; margin-top: 30px;">
                            <a href="http://{settings.ALLOWED_HOSTS[0] if settings.ALLOWED_HOSTS and settings.ALLOWED_HOSTS[0] != '*' else '127.0.0.1:8000'}/dashboard/manager/" 
                               style="background-color: #2563eb; color: white; padding: 12px 24px; border-radius: 10px; text-decoration: none; font-size: 12px; font-weight: bold; display: inline-block;">
                                ACCESS MANAGEMENT DASHBOARD
                            </a>
                        </div>
                    </div>
                </body>
            </html>
            """

            try:
                send_mail(
                    subject=subject,
                    message=text_body,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=recipients,
                    html_message=html_body,
                    fail_silently=False,
                )
                self.stdout.write(self.style.SUCCESS(
                    f"Successfully delivered summary update to {recipients} for {platform.platform_name}"))
            except Exception as error:
                self.stdout.write(
                    self.style.ERROR(f"Delivery structural error sending emails to {recipients}: {str(error)}"))