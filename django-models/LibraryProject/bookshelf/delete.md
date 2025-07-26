``` shell 
from bookshelf.models import Book
book = Book.objects.first()

book.delete()
# Output: (1, {'bookshelf.Book': 1})

# Confirm deletion by trying to retrieve all books again
Book.objects.all()
# Output: <QuerySet []>
```