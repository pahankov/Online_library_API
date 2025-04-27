from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    year = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return f"{self.title} ({self.author})"


class Order(models.Model):
    user_name = models.CharField(max_length=150)
    days_count = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return f"Order #{self.id} by {self.user_name}"
