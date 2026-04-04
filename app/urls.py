from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.home, name='home'),
    path('main/catalog/', views.catalog, name='catalog'),
    path('main/', views.main, name='main'),
    path('movies/', views.movies, name='movies')
]