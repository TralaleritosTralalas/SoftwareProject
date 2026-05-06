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
    path('personal_library/',views.personal_library, name='personal_library'),
    path('user_settings/',views.user_settings, name='user_settings'),
    path('onboarding/', views.onboarding, name='onboarding'),
    path('onboarding/genres/', views.onboarding_genres, name='onboarding_genres'),
    path('onboarding-complete/', views.onboarding_complete, name='onboarding_complete'),
    path('dashboard/direction/', views.direction_dashboard, name='direction_dashboard'),
    path('content/<str:ctype>/<int:cid>/', views.content_detail, name='content_detail'),
]
