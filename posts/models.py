
from enum import unique
from django.db import models
from django.db.models import Model
from django.db.models.deletion import CASCADE
from ckeditor.fields import RichTextField
from datetime import datetime
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files import File
from django.http import request
from django.urls import reverse
from PIL import Image


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.title

class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100, default='Shezan MAhmud')
    isbn = models.CharField(max_length=13)
    pages = models.IntegerField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    description = models.TextField()
    details =  RichTextField(blank=True, null=True)
    status = models.BooleanField()
    date_created = models.DateField(auto_now_add=True)
    photo = models.ImageField(upload_to='books/photo')
    

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title

class Grocery(models.Model):
    product_tag = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='grocery', on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()
    imageurl = models.URLField()
    status = models.BooleanField()
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.name