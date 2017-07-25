from django.views.decorators.csrf import csrf_protect
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, Http404, redirect, HttpResponse
from .models import DiaryPage, Category
from django.contrib import auth
# Create your views here.

def main_screen(request, page_number=1):
    diary_pages = DiaryPage.objects.all().order_by('-id')
    categories = Category.objects.filter(author=auth.get_user(request))

    current_page = Paginator(diary_pages, 50)
    args = {}
    args['diary_pages'] = current_page.page(page_number)
    args['user'] = auth.get_user(request)
    if categories:
        args['categories'] = categories
    else:
        return render(request, 'ERROR_PERMISSION.html')
    return render(request, 'diary/main_screen/main.html', args)



'''
    args = {}
    args['user'] = auth.get_user(request)
    args['post'] = post
    args['author'] = post.author
    args['category'] = post.category
    args['title'] = post.title
    args['img'] = post.img
    args['text'] = post.text_rich
    args['when_happened'] = post.when_happened
    args['published_date'] = post.published_date
    
'''