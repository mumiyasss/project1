from django.test import TestCase
from django.shortcuts import render, redirect
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
# Create your tests here.

class ManyUsers(TestCase):
    def creating_alot(self):
        for i in range(0, 1000):
            ii = str(i)
            username = 'username'+ii
            email = 'email@mail.ru'+ii
            password1 = 'PAAsword'+ii
            # Сохранение пользователя
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.save()
            print(ii)
            user = auth.authenticate(username=username, password=password1)
