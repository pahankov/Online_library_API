from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book, Order

class BookAPITests(APITestCase):
    def setUp(self):
        self.book = Book.objects.create(
            title="Test Book",
            author="Test Author",
            year=2021,
            description="Test Description"
        )

    def test_get_book_list(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_book(self):
        url = reverse('book-create')
        data = {
            "title": "New Book",
            "author": "New Author",
            "year": 2023,
            "description": "New Description"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class OrderAPITests(APITestCase):
    def setUp(self):
        self.book1 = Book.objects.create(title="Book 1", author="Author 1", year=2000)
        self.book2 = Book.objects.create(title="Book 2", author="Author 2", year=2001)
        self.order = Order.objects.create(user_name="Test User", days_count=5)
        self.order.books.add(self.book1)

    def test_create_order(self):
        url = reverse('order-list')
        data = {
            "user_name": "New User",
            "days_count": 7,
            "book_ids": [self.book1.id, self.book2.id]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
