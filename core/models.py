"""
Models for Library API.
"""

from django.db import models

class Category(models.Model):
    """
    Model for book categories.
    """
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Return string representation of the category.
        """
        return self.name

class Book(models.Model):
    """
    Model for books.
    """

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    no_of_pages = models.PositiveIntegerField()
    description = models.TextField()
    category = models.ForeignKey(Category, related_name='books', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Return string representation of the book.
        """
        return self.title
