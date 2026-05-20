from app.models import Notification


def unread_notifications(request):
    if not request.user.is_authenticated:
        return {}
    notifications = Notification.objects.filter(
        user=request.user, seen=False
    ).order_by('-id')[:10]
    return {
        'unread_notifications': notifications,
        'unread_count': notifications.count(),
    }
