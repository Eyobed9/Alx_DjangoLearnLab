from relationship_app.models import Author, Book, Library;

# Query all books by a specific author
books = Book.objects.filter(author__name="John Doe")
print(books)

# List all books in a library
library = Library.objects.get(name=library_name) 
books = library.books.all()
print(books)

# Retrieve the librarian for a library
librarian = library.librarian
print(librarian)

# Create a new book
adam = Author(name="adam")
adam.save()
new_book = Book(title='Genesis', author=adam)
new_book.save()