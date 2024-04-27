from django.contrib import admin

# Register your models here.
from .models import Book, Category

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'no_of_pages', 'category', 'created_at', 'updated_at')
    #search_fields = ('title', 'author', 'category')
    #list_filter = ('category', 'created_at', 'updated_at')
    
admin.site.register(Book)
admin.site.register(Category)
