from django.urls import path, include
from .views import ProfileView, ProfileUpdateView
from django.contrib.auth.views import LogoutView
from .views import RegisterView, LoginView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="api_register"),
    path("login/", LoginView.as_view(), name="api_login"),
    path("profile/", ProfileView.as_view(), name="profile",),
    path("profile/update", ProfileUpdateView.as_view(), name="profile_update"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
