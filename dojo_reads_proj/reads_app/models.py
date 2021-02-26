from django.db import models
from login_app.models import User



class Book(models.Model):
    title = models.CharField(max_length=255)
    users = models.ManyToManyField(User, related_name="reviewed_books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Author(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name="authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Review(models.Model):
    rating = models.IntegerField()
    comment = models.TextField()
    book = models.ForeignKey(Book, related_name="reviews", on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name="reviews", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



