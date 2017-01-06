from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.views.decorators.csrf import csrf_protect
#from django.middleware import csrf
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import User
from .logic import SiteUserPreferences
from . import messages
# Create your views here.

@csrf_protect
def login(request):
    args = {}
    #args.update(csrf(request))
    args['page_title'] = messages.loginPageTitle
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = messages.loginError
            return render_to_response("loginsys/login.html", args)
    else:
        return render_to_response('loginsys/login.html', args)


def logout(request):
    auth.logout(request)
    return redirect("/")

@csrf_protect
def register(request):
    args = {}
    #args.update(csrf(request))
    args['page_title'] = messages.registerPageTitle
    if request.POST:
        email = request.POST.get('email', '')
        username = request.POST.get('username', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        # Проверка на ошибки
        tools = SiteUserPreferences() # из пакета logic.py
        errors = tools.validation(username=username, email=email,
                                     password1=password1, password2=password2)
        if errors:
            args['register_error'] = errors
            return render_to_response("loginsys/register.html", args)
        # Сохранение пользователя
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        # Автроризируемся!
        user = auth.authenticate(username=username, password=password1)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = messages.loginError
            return render_to_response("loginsys/register.html", args)
    else:
        return render_to_response('loginsys/register.html', args)