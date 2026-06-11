from django.urls import path
from . import views, admin
app_name = 'app'

urlpatterns = [
    path('', views.home, name='home'),
    path('main/', views.main, name='main'),
    path('catalog/', views.catalog, name='catalog'),
    path('movies/', views.movies, name='movies'),
    path('series/', views.series, name='series'),
    path('search/', views.search, name='search'),
    path('redirect/',views.login_redirect, name='login_redirect'),
    path('content/<str:ctype>/<str:cid>/', views.content_detail, name='content_detail'),
    path('content/<str:ctype>/<str:cid>/update-status/', views.update_status, name='update_status'),
    path('content/<str:ctype>/<str:cid>/toggle-favorite/', views.toggle_favorite, name='toggle_favorite'),
    path('content/<str:ctype>/<str:cid>/add-to-list/<int:list_id>/', views.add_to_list, name='add_to_list'),
    path('content/<str:ctype>/<str:cid>/remove-from-list/<int:list_id>/', views.remove_from_list, name='remove_from_list'),
    path('personal_library/',views.personal_library, name='personal_library'),
    path('personal_library/list/<int:list_id>/', views.list_detail, name='list_detail'),
    path('user_settings/',views.user_settings, name='user_settings'),
    path('onboarding/', views.onboarding, name='onboarding'),
    path('onboarding/genres/', views.onboarding_genres, name='onboarding_genres'),
    path('onboarding-complete/', views.onboarding_complete, name='onboarding_complete'),
    path('delete_account/', views.delete_account, name='delete_account'),
    path('dashboard/direction/', views.direction_dashboard, name='direction_dashboard'),
    
    path('api/notifications/mark-seen/', views.mark_notification_seen, name='mark_notification_seen'),
    path('dashboard/manager/', views.manager_dashboard, name='manager_dashboard'),
    path('content/<str:ctype>/<int:cid>/', views.content_detail, name='content_detail'),
    path('api/watchlist/lists/', views.get_user_lists, name='get_user_lists'),
    path('api/watchlist/lists/create/', views.create_list, name='create_list'),
    path('api/watchlist/lists/<int:list_id>/rename/', views.rename_list, name='rename_list'),
    path('api/watchlist/lists/<int:list_id>/', views.delete_list, name='delete_list'),
]
