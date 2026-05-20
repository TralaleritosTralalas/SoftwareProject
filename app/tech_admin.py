from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from django.contrib.admin import AdminSite
from . import views
from django.urls import path


class TechUserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'get_role', 'is_staff')
    list_filter = ('role', 'is_staff')
    search_fields = ('username', 'email')
    ordering = ('username',)
    list_per_page = 10

    def get_role(self, obj):
        return obj.role

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

        try:
            custom_user = User.objects.select_related('role').get(pk=request.user.pk)
            if custom_user.role:
                return custom_user.role.name.lower() == 'technical'
        except User.DoesNotExist:
            return False

        return False

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('auth/user/add/', self.admin_view(views.tech_add_user_view), name='auth_user_add'),
            path('auth/user/<int:user_id>/change/', self.admin_view(views.tech_edit_user_view),
                 name='auth_user_change'),
            path('auth/user/<int:user_id>/delete/', self.admin_view(views.tech_delete_user), name='auth_user_delete'),
        ]
        return custom_urls + urls

    def index(self, request, extra_context=None):
        from django.contrib.auth.models import Group

        users = User.objects.all().select_related('role')

        query = request.GET.get('q')
        if query:
            users = users.filter(username__icontains=query) | users.filter(email__icontains=query)

        role_filter = request.GET.get('role')
        if role_filter:
            users = users.filter(role_id=role_filter)

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


tech_admin_site = TechAdminSite(name='tech_admin')
tech_admin_site.register(User, TechUserAdmin)
