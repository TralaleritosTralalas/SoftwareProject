from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from django.contrib.auth import views as auth_views
from .forms import CustomUserCreationForm


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("app:onboarding")
    template_name = "registration/singup.html"


def terms_of_service(request):
    return render(request, "registration/terms_of_service.html")


def privacy_policy(request):
    return render(request, "registration/privacy_policy.html")

password_reset = auth_views.PasswordResetView.as_view(
    template_name='registration/password_reset_form.html',
    success_url=reverse_lazy('password_reset_done')
)

password_reset_done = auth_views.PasswordResetDoneView.as_view(
    template_name='registration/password_reset_done.html'
)

password_reset_confirm = auth_views.PasswordResetConfirmView.as_view(
    template_name='registration/password_reset_confirm.html',
    success_url=reverse_lazy('password_reset_complete')
)

password_reset_complete = auth_views.PasswordResetCompleteView.as_view(
    template_name='registration/password_reset_complete.html'
)