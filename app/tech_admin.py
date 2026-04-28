from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Profile
from django.contrib.admin import AdminSite
from . import views
from django.urls import path



class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Información del Perfil'

class TechUserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
    list_display = ('username', 'email', 'get_role', 'is_staff')
    list_filter = ('profile__role', 'is_staff')
    search_fields = ('username', 'email')
    ordering = ('username',)
    list_per_page = 10  # Paginación automática

    def get_role(self, obj):
        return obj.profile.role
    get_role.short_description = 'Rol'

    

class TechAdminSite(AdminSite):
    site_header = "StreamSync Tech"
    index_template = 'admin/tech.html'
    change_form_template = 'admin/tech_change_form.html'
    add_form_template = 'admin/tech_add_form.html'

    def has_permission(self, request):
        if not request.user.is_authenticated or not request.user.is_active:
            return False
        
        if request.user.is_superuser:
            return True

        profile = getattr(request.user, 'profile', None)
        if profile and profile.role:
            return profile.role.name.lower() == 'technical'
        
        return False
                
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('auth/user/add/', self.admin_view(views.tech_add_user_view), name='auth_user_add'),
            path('auth/user/<int:user_id>/change/', self.admin_view(views.tech_edit_user_view), name='auth_user_change'),
            path('auth/user/<int:user_id>/delete/', self.admin_view(views.tech_delete_user), name='auth_user_delete'),
        ]
        return custom_urls + urls
    
    def index(self, request, extra_context=None):
        from django.contrib.auth.models import User, Group
        
        users = User.objects.all().select_related('profile')

        query = request.GET.get('q')
        if query:
            users = users.filter(username__icontains=query) | users.filter(email__icontains=query)

        role_filter = request.GET.get('role')
        if role_filter:
            users = users.filter(profile__role_id=role_filter)

        status_filter = request.GET.get('status')

        if status_filter == 'active':
            users = users.filter(is_active=True)

        elif status_filter == 'inactive':
            users = users.filter(is_active=False)

        extra_context = extra_context or {}
        extra_context['tech_users'] = users.order_by('-date_joined')[:10]
        extra_context['groups'] = Group.objects.all()
        
        extra_context['current_role'] = role_filter
        extra_context['current_status'] = status_filter

        return super().index(request, extra_context)

tech_site = TechAdminSite(name='tech_admin')
tech_site.register(User, TechUserAdmin)