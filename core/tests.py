from django.test import TestCase
from rest_framework.test import APIClient
from .models import Category, Book

class CategoryTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.category1 = Category.objects.create(name='Fiction')
        self.category2 = Category.objects.create(name='Science')

    def test_category_list(self):
        response = self.client.get('/categories/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_category_detail(self):
        response = self.client.get(f'/categories/{self.category1.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'Fiction')

    def test_category_create(self):
        response = self.client.post('/categories/', {'name': 'Horror'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Category.objects.count(), 3)

    # Add tests for update and delete functionalities

class BookTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.category = Category.objects.create(name='Fiction')
        self.book = Book.objects.create(
            title='Example Book',
            author='John Doe',
            no_of_pages=200,
            description='An example book description',
            category=self.category
        )

    def test_book_list(self):
        response = self.client.get('/books/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_book_detail(self):
        response = self.client.get(f'/books/{self.book.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'Example Book')

    def test_book_create(self):
        response = self.client.post('/books/', {
            'title': 'New Book',
            'author': 'Jane Smith',
            'no_of_pages': 150,
            'description': 'A new book description',
            'category': self.category.id
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Book.objects.count(), 2)