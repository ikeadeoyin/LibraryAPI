from django.urls import path
from .views import CategoryList, CategoryDetail, BookList, BookDetail

urlpatterns = [
    path('categories/', CategoryList.as_view(), name='category_list'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category_detail'),
    path('books/', BookList.as_view(), name='book_list'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book_detail'),
]