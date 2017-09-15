from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from mysite.settings import MEDIA_ROOT
from ckeditor.fields import RichTextField
# Create your models here.


class Post(models.Model):
    author   = models.ForeignKey('auth.User')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=False, blank=False)
    title    = models.CharField(max_length=200)
    # Содержание
    text = models.TextField()
    img = models.ImageField(upload_to='images/post/', null=True, blank=True)

    def intro(self): # Это можно оптимизировать записью в базу при методе save 
        temp_text = str(self.text)
        intro_text = temp_text[:140] # Только первые 140 символов
        # В конце должны быть пробел и многоточие...
        if intro_text[len(intro_text)-1] == ' ':
            return (intro_text + '...')
        else:
            return (intro_text + ' ' + '...')

    # Что-то о времени
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        default=timezone.now, blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class CommentsManager(models.Manager):
    def create_comment(self, text, author, post):
        comment = self.create(text=text, author=author, post=post)
        return comment


class Comments(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, null=False)
    author = models.ForeignKey('auth.User')
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    objects = CommentsManager()

    def publish(self):
        self.created_date = timezone.now()
        self.save()


class LikesManger(models.Model):
    def create_like(self, user):
        like = self.create(user=user)
        return like


class Likes(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, null=False)
    user = models.ForeignKey('auth.User')
    objects = LikesManger()

    def __str__(self):
        return self.user.username
