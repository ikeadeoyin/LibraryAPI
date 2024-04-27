from django.test import TestCase
from .models import Book, Category
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .serializers import BookSerializer, CategorySerializer

class BookModelTest(TestCase):  
    def setUp(self):
        Category.objects.create(name='Fiction')
        Category.objects.create(name='Non-Fiction')
        Book.objects.create(title='Book1', author='Author1', no_of_pages=100, description='Description1', category=Category.objects.get(id=1))
        Book.objects.create(title='Book2', author='Author2', no_of_pages=200, description='Description2', category=Category.objects.get(id=2))
        
    def test_book_model(self):
        book1 = Book.objects.get(title='Book1')
        book2 = Book.objects.get(title='Book2')
        self.assertEqual(book1.author, 'Author1')
        self.assertEqual(book2.author, 'Author2')
        self.assertEqual(book1.no_of_pages, 100)
        self.assertEqual(book2.no_of_pages, 200)
        self.assertEqual(book1.description, 'Description1')
        self.assertEqual(book2.description, 'Description2')
        self.assertEqual(book1.category.name, 'Fiction')
        self.assertEqual(book2.category.name, 'Non-Fiction')

class CategoryModelTest(TestCase):  
    def setUp(self):
        Category.objects.create(name='Fiction')
        Category.objects.create(name='Non-Fiction')
        
    def test_category_model(self):
        category1 = Category.objects.get(name='Fiction')
        category2 = Category.objects.get(name='Non-Fiction')
        self.assertEqual(category1.name, 'Fiction')
        self.assertEqual(category2.name, 'Non-Fiction')


class BookAPITest(APITestCase):
    def setUp(self):
        Category.objects.create(name='Fiction')
        Category.objects.create(name='Non-Fiction')
        Book.objects.create(title='Book1', author='Author1', no_of_pages=100, description='Description1', category=Category.objects.get(id=1))
        Book.objects.create(title='Book2', author='Author2', no_of_pages=200, description='Description2', category=Category.objects.get(id=2))
        
    def test_get_books(self):
        response = self.client.get(reverse('books:book-list'))
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_get_categories(self):
        response = self.client.get(reverse('books:category-list'))
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_create_book(self):
        data = {
            'title': 'Book3',
            'author': 'Author3',
            'no_of_pages': 300,
            'description': 'Description3',
            'category': 1
        }
        response = self.client.post(reverse('books:book-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_create_category(self):
        data = {
            'name': 'Horror'
        }
        response = self.client.post(reverse('books:category-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_update_book(self):
        data = {
            'title': 'Book3',
            'author': 'Author3',
            'no_of_pages': 300,
            'description': 'Description3',
            'category': 1
        }
        response = self.client.put(reverse('books:book-detail', kwargs={'pk': 1}), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_update_category(self):
        data = {
            'name': 'Horror'
        }
        response = self.client.put(reverse('books:category-detail', kwargs={'pk': 1}), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_delete_book(self):
        response = self.client.delete(reverse('books:book-detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

# Create your tests here.
