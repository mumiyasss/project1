from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from mysite.settings import MEDIA_ROOT
# Create your models here.

class Post(models.Model):
    author   = models.ForeignKey('auth.User')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=False)
    title    = models.CharField(max_length=200)
    # Содержание
    text = models.TextField()
    img = models.ImageField(upload_to='images/post/', null=True)

    def intro(self):
        temp_text = str(self.text)
        intro_text = temp_text[:140] # Только первые 140 символов
        ### В конце должны быть пробел и многоточие...
        if intro_text[len(intro_text)-1] == ' ':
            return (intro_text + '...')
        else:
            return (intro_text + ' ' + '...')

    # Что-то о времени
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    # Рейтинг
    likes = models.IntegerField(default=0)
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

class Likers(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, null=False)
    user = User()

    def __str__(self):
        return self.user.username