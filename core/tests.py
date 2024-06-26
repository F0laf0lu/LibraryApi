"""
Tests for the Library API.
"""

from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse

from .models import Category, Book

class CategoryTestCase(TestCase):
    """
    Tests for Category model.
    """

    def setUp(self):
        self.client = APIClient()
        self.category1 = Category.objects.create(name='Fiction')
        self.category2 = Category.objects.create(name='Science')

    def test_category_list(self):
        """
        Test retrieving all categories.
        """
        url = reverse("category-list-create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_category_detail(self):
        """
        Test retrieving details of a category.
        """
        url = reverse("category-detail", kwargs={"pk":self.category1.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'Fiction')

    def test_category_create(self):
        """
        Test creating a new category.
        """
        url = reverse("category-list-create")
        data = {'name': 'Horror'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Category.objects.count(), 3)

    def test_category_update(self):
        """
        Test updating a category.
        """
        url = reverse("category-detail", kwargs={"pk":self.category1.id})
        data = {'name': 'Fantasy'}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Category.objects.get(id=self.category1.id).name, 'Fantasy')

    def test_category_delete(self):
        """
        Test deleting a category.
        """
        url = reverse("category-detail", kwargs={"pk":self.category1.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertIsNone(Category.objects.filter(id=self.category1.id).first())

class BookTestCase(TestCase):
    """
    Tests for Book model.
    """
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
        """
        Test retrieving all books.
        """
        url = reverse('book-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_book_detail(self):
        """
        Test retrieving details of a book.
        """
        url = reverse('book-detail', kwargs={"pk":self.book.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'Example Book')

    def test_book_create(self):
        """
        Test creating a new book.
        """
        url = reverse('book-list-create')
        data = {
            'title': 'New Book',
            'author': 'Jane Smith',
            'no_of_pages': 150,
            'description': 'A new book description',
            'category': self.category.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Book.objects.count(), 2)

    def test_book_update(self):
        """
        Test creating a new book.
        """
        url = reverse('book-detail', kwargs={"pk":self.book.id})
        data =  {'title': 'Updated Book'}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Book.objects.get(id=self.book.id).title, 'Updated Book')

    def test_book_delete(self):
        """
        Test deleting a book.
        """
        url = reverse('book-detail', kwargs={"pk":self.book.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertIsNone(Book.objects.filter(id=self.book.id).first())
    
    def test_book_catgory_set_to_null_ondeletete(self):
        url = reverse("category-detail", kwargs={"pk":self.category.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.book.refresh_from_db() 
        self.assertIsNone(self.book.category)
