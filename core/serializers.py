"""
Serializers for Library API.
"""

from rest_framework import serializers
from .models import Category, Book

class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for Category model.
    """

    class Meta:
        """
        Meta class for CategorySerializer.
        """
        model = Category
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for Book model.
    """

    class Meta:
        """
        Meta class for BookSerializer.
        """
        model = Book
        fields = '__all__'
