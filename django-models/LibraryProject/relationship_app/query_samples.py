from relationship_app.models import Author, Book, Library, Librarian;

# Query all books by a specific author
author = Author.objects.get(name=author_name)
books = Book.objects.filter(author=author)
print(books)

# List all books in a library
library = Library.objects.get(name=library_name) 
books = library.books.all()
print(books)

# Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)
print(librarian)

# Create a new book
adam = Author(name="adam")
adam.save()
new_book = Book(title='Genesis', author=adam)
new_book.save()