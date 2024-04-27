from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    no_of_pages = models.PositiveIntegerField()
    description = models.TextField()
    category = models.ForeignKey(Category, related_name='books', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} - {self.category}'
    