from django.contrib import admin
from posts.models import Category, Book, Grocery

# Register your models here.

admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Grocery)