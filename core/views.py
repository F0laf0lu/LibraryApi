"""
Views for Library API.
"""

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from .models import Category, Book
from .serializers import CategorySerializer, BookSerializer


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
    """
    API view for listing and creating categories.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a category.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BookListCreateAPIView(generics.ListCreateAPIView):
    """
    API view for listing and creating books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
