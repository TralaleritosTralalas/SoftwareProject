from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render

from .forms import CustomUserCreationForm


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/singup.html"


def terms_of_service(request):
    return render(request, "registration/terms_of_service.html")


def privacy_policy(request):
    return render(request, "registration/privacy_policy.html")