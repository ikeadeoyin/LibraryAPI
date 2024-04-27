from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Book, Category
from .serializers import BookSerializer, CategorySerializer

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# class CategoryRetrieveAPIView(generics.RetrieveAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
