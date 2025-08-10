from django.urls import path
from .views import (
    list_books,
    LibraryDetailView,
    user_login,
    user_logout,
    user_register,
    admin_view,
    librarian_view,
    member_view,
    # add_book,
    # edit_book,
    # delete_book,
)

urlpatterns = [
    path("books/", list_books, name="list-books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library-detail"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("register/", user_register, name="register"),
    path("admin-role/", admin_view, name="admin_view"),
    path("librarian-role/", librarian_view, name="librarian_view"),
    path("member-role/", member_view, name="member_view"),
    # path("books/add/", add_book, name="add_book"),
    # path("books/edit/<int:pk>/", edit_book, name="edit_book"),
    # path("books/delete/<int:pk>/", delete_book, name="delete_book"),
]
# LibraryProject/relationship_app/urls.py doesn't contain: ["views.register", "LogoutView.as_view(template_name=", "LoginView.as_view(template_name="]
# "add_book/", "edit_book/"]

# ["add_book/", "edit_book/"]
