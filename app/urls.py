from django.urls import path
from . import views, admin

app_name = 'app'

urlpatterns = [
    path('', views.home, name='home'),
    path('catalog/', views.catalog, name='catalog'),
    path('main/', views.main, name='main'),
    path('movies/', views.movies, name='movies'),
    path('series/', views.series, name='series'),
    path('search/', views.search, name='search'),
    path('redirect/',views.login_redirect, name='login_redirect'),
    path('content/<str:ctype>/<int:cid>/', views.content_detail, name='content_detail'),
  
]
