from django.urls import path
from .views import SignUpView, terms_of_service, privacy_policy

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("terms-of-service/", terms_of_service, name="terms_of_service"),
    path("privacy-policy/", privacy_policy, name="privacy_policy"),
]