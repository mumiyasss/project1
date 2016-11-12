from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    author   = models.ForeignKey('auth.User')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=False)
    title    = models.CharField(max_length=200)
    # Содержание
    text = models.TextField()

    # Что-то о времени
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Comments(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, null=False)
    author = models.ForeignKey('auth.User')
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)


    def publish(self):
        self.created_date = timezone.now()
        self.save()