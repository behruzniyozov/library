from django.test import TestCase
from django.urls import reverse

from .models import Book

class BookTestCase(TestCase):
    def setUp(self):
        self.book = Book.objects.create(
            title='Test Book',
            subtitle='Test Subtitle',
            author='Test Author',
            isbn='1234567890123'
        )

    def test_book_content(self):
        self.assertEqual(self.book.title, 'Test Book')
        self.assertEqual(self.book.subtitle, 'Test Subtitle')
        self.assertEqual(self.book.author, 'Test Author')
        self.assertEqual(self.book.isbn, '1234567890123')

    def test_book_str(self):
        self.assertEqual(str(self.book), 'Test Book')

    def test_book_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/book_list.html')
        self.assertContains(response, 'Test Book')
