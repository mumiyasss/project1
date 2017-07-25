from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from mysite.settings import MEDIA_ROOT
from ckeditor.fields import RichTextField
# Create your models here.


class DiaryPage(models.Model):
    author   = models.ForeignKey('auth.User')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=False, blank=False)
    title    = models.CharField(max_length=200)
    # Содержание
    text_rich = RichTextField(blank=True, default='')
    #img = models.ImageField(upload_to='images/post/', null=True, blank=True)

    def intro(self): # Это можно оптимизировать записью в базу при методе safe
        temp_text = str(self.text_rich)
        intro_text = temp_text[:140] # Только первые 140 символов
        # В конце должны быть пробел и многоточие...
        if intro_text[len(intro_text)-1] == ' ':
            return (intro_text + '...')
        else:
            return (intro_text + ' ' + '...')

    # Что-то о времени
    when_happened = models.DateTimeField(
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
    ticket_colour = models.CharField(max_length=15)
    author = models.ForeignKey('auth.User')

    def __str__(self):
        return self.title