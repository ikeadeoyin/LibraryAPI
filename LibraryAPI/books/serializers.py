from rest_framework import serializers
from .models import Book, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'no_of_pages', 'description', 'category',)
