from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'role', 'country', 'age', 'is_staff')
    list_filter = ('role', 'country', 'is_staff')
    fieldsets = (
        ('User information', {'fields': ('username', 'password')}),
        ('Personal user information', {'fields': ('first_name', 'last_name', 'email')}),
        ('Extra information', {'fields': ('role', 'birth_date', 'country', 'profile_picture')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Dates related info', {'fields': ('last_login', 'date_joined')}),
    )


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'genre', 'rating', 'duration_minutes')
    search_fields = ('title', 'synopsis')
    list_filter = ('year', 'genre', 'age_rating')


@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_year', 'end_year', 'total_seasons', 'rating')
    list_filter = ('start_year', 'genre')


@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ('platform', 'content', 'state')
    list_filter = ('platform', 'state')


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'birth_date')


@admin.register(Statistics)
class StatisticsAdmin(admin.ModelAdmin):
    list_display = ('platform', 'week', 'total_favorites', 'total_clicks')
    readonly_fields = ('total_favorites', 'total_clicks')


@admin.register(VisualizationProgress)
class VisualizationProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'last_minute', 'completed')
    list_filter = ('completed',)


admin.site.register(Country)
admin.site.register(Genre)
admin.site.register(AgeRating)
admin.site.register(Language)
admin.site.register(Platform)
admin.site.register(Notification)
admin.site.register(Favorite)
admin.site.register(Watchlist)
