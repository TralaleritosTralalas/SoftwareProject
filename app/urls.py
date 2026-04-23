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
    path('content/<str:ctype>/<int:cid>/', views.content_detail, name='content_detail'),
    path('personal_library/',views.personal_library, name='personal_library'),
    path('user_settings/',views.user_settings, name='user account settings'),
]
