from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)
    published_date = models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]


class Library(models.Model):
    name = models.CharField(max_length=50)
    books = models.ManyToManyField(Book, related_name="libraries")

    def __str__(self):
        return self.name


class Librarian(models.Model):
    name = models.CharField(max_length=50)
    library = models.OneToOneField(
        Library, related_name="librarian", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


# # LibraryProject/relationship_app/urls.py doesn't contain: ["views.register", "LogoutView.as_view(template_name=", "LoginView.as_view(template_name="]
# LibraryProject/relationship_app/models.py doesn't contain: ["class UserProfile(models.Model):", "Admin", "Member"]
