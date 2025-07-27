from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from .models import Book, Library

def list_books(request):
    books = Book.objects.select_related('author').all()
    return render(request, "list_books.html", {"books": books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = "library_detail.html"
    context_object_name = "library"
# relationship_app/list_books.html", "Book.objects.all()"]
# "relationship_app/library_detail.html", "from .models import Library"

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("list-books")  # or any homepage
    else:
        form = AuthenticationForm()
    return render(request, "relationship_app/login.html", {"form": form})


def user_register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})


def user_logout(request):
    logout(request)
    return render(request, "relationship_app/logout.html")
