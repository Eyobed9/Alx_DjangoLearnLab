from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Author, Book
from .serializers import BookSerializer
from django.contrib.auth.models import User

class BookAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.author = Author.objects.create(name="J.R.R. Tolkien")
        self.book1 = Book.objects.create(title="The Hobbit", author=self.author, publication_year=1937)
        self.book2 = Book.objects.create(title="The Lord of the Rings", author=self.author, publication_year=1954)
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)

    def test_book_list(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer_data = BookSerializer([self.book1, self.book2], many=True).data
        self.assertEqual(response.data, serializer_data)

    def test_book_detail(self):
        url = reverse('book-detail', args=[self.book1.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer_data = BookSerializer(self.book1).data
        self.assertEqual(response.data, serializer_data)

    def test_book_create(self):
        url = reverse('book-create')
        data = {'title': 'The Silmarillion', 'author': self.author.pk, 'publication_year': 1977}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.get(title='The Silmarillion').publication_year, 1977)

    def test_book_update(self):
        url = reverse('book-update', args=[self.book1.pk])
        data = {'title': 'The Hobbit Updated', 'author': self.author.pk, 'publication_year': 1937}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.get(pk=self.book1.pk).title, 'The Hobbit Updated')

    def test_book_delete(self):
        url = reverse('book-delete', args=[self.book1.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_book_list_filter_title(self):
        url = reverse('book-list') + '?title=The Hobbit'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'The Hobbit')

    def test_book_list_search_author(self):
        url = reverse('book-list') + '?search=Tolkien'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Both books should match

    def test_book_list_ordering_title(self):
        url = reverse('book-list') + '?ordering=title'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        titles = [book['title'] for book in response.data]
        self.assertEqual(titles, sorted(titles))  # Check if titles are sorted

    def test_permission_unauthenticated_list(self):
        self.client.logout()
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_permission_unauthenticated_create(self):
        self.client.logout()
        url = reverse('book-create')
        data = {'title': 'The Silmarillion', 'author': self.author.pk, 'publication_year': 1977}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN) # Or 401, depending on your auth setup