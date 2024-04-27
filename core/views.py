"""
Views for Library API.
"""

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from .models import Category, Book
from .serializers import (
    CategoryReadSerializer,
    CategoryWriteSerializer,
    BookReadSerializer,
    BookWriteSerializer
)

class ApiRoot(APIView):
    """
    API root view.
    """

    def get(self, request, format=None):
        """
        Return a response with links to API resources.
        """
        return Response({
            'categories': reverse('category-list-create', request=request, format=format),
            'books': reverse('book-list-create', request=request, format=format),
        })


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CategoryReadSerializer
        else:
            return CategoryWriteSerializer

class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CategoryReadSerializer
        else:
            return CategoryWriteSerializer


class BookListCreateAPIView(generics.ListCreateAPIView):
    """
    API view for listing and creating books.
    """
    queryset = Book.objects.all()

    def get_serializer_class(self):
        """
        Return the appropriate serializer class based on the request method.
        """
        if self.request.method == 'GET':
            return BookReadSerializer
        else:
            return BookWriteSerializer

class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a book.
    """
    queryset = Book.objects.all()

    def get_serializer_class(self):
        """
        Return the appropriate serializer class based on the request method.
        """
        if self.request.method == 'GET':
            return BookReadSerializer
        else:
            return BookWriteSerializer