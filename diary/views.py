from django.views.decorators.csrf import csrf_protect
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, Http404, redirect, HttpResponse
from .models import DiaryPage, Category
from django.contrib import auth
# Create your views here.

def main_screen(request):
    
    categories = Category.objects.filter(author=auth.get_user(request))
    args = {}
    args['user'] = auth.get_user(request)
    if categories:
        args['categories'] = categories
    else:
        return render(request, 'ERROR_PERMISSION.html')
    return render(request, 'diary/main_screen/main.html', args)


def cat_posts_list(request, cat_id, page_number=1):
    args = {}
    diary_pages = DiaryPage.objects.all().order_by('-id')
    current_page = Paginator(diary_pages, 50)
    args['diary_pages'] = current_page.page(page_number)
    return render(request, 'diary/cat_posts_list/main.html', args)

def view_post(request, post_id):
    args = {}
    try:
        post = get_object_or_404(DiaryPage, pk=post_id)
    except Http404:
        return render(request, 'ERROR_404.html')
    args['post'] = post
    return render(request, 'diary/view_post/main.html', args)

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