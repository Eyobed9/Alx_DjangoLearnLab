from django.urls import path, include
from .views import SignUpView, ProfileView, ProfileUpdateView, PostListView, PostDetailView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("register/", SignUpView.as_view(), name="templates/registration/signup"),
    path(
        "profile/",
        ProfileView.as_view(),
        name="profile",
    ),
    path(
        "login/",
        LoginView.as_view(template_name="registration/login.html", next_page="profile"),
        name="login",
    ),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/update", ProfileUpdateView.as_view(), name="profile_update"),
    path("posts/", PostListView.as_view(), name="post_list"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    #  path("tags/<slug:tag>/", PostByTagListView.as_view(), name="posts-by-tag"),
    # post/<int:pk>/delete/", "post/<int:pk>/update/", "post/new/
]
