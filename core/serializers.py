"""
Serializers for Library API.
"""

from rest_framework import serializers
from .models import Category, Book


class CategoryReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name','created_at', 'updated_at']

class CategoryWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ['created_at', 'updated_at']

class BookReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'no_of_pages', 'description', 'category', 'created_at','updated_at']

class BookWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        exclude = ['created_at','updated_at']

