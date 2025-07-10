``` shell 
from bookshelf.models import Book
book = Book.objects.first()

print(book.title)  # Output: "1984"
print(book.author)  # Output: "George Orwell"   
print(book.publication_year)  # Output: 1949
```