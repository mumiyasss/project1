from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import User
# Create your views here.

def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = "Пользователь не найден"
            return render_to_response("loginsys/login.html", args)
    else:
        return render_to_response('loginsys/login.html', args)


def logout(request):
    auth.logout(request)
    return redirect("/")


def register(request):
    args = {}
    args.update(csrf(request))
    args['page_title'] = "Регистрация"
    if request.POST:
        email = request.POST.get('email', '')
        username = request.POST.get('username', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        if password1 and password2 and password1 != password2:
            args['register_error'] = "Пароли не совпадают!"
            return render_to_response("loginsys/register.html", args)
        #strU = str(username)
        #strE = str(email)
        #strP = str(password1)
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        user = auth.authenticate(username=username, password=password1)
        #user = UserManager()
        #user.create_user(username=email, email=email, password=password1)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['register_error'] = "Пользователь не найден"
            return render_to_response("loginsys/register.html", args)
    else:
        return render_to_response('loginsys/register.html', args)