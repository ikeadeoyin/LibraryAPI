from django.db import models

# Create your models here.
# title(str),
# author(str),
# no_of_pages(int),
# description(text),
# category(FK)
# created_at(datetime),
# updated_at(datetime)


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    no_of_pages = models.IntegerField()
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Category(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name