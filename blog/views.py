from django.shortcuts import render, get_object_or_404, Http404, redirect, HttpResponse
from .models import Post, Comments
from django.contrib import auth
from .forms import CommentForm, NewPostForm
from django.core.context_processors import csrf
from django.core.paginator import Paginator
from mysite.settings import MEDIA_ROOT
# Create your views here.


def index_list(request, page_number=1):
    posts = Post.objects.all()
    current_page = Paginator(posts, 2)
    args = {}
    args['posts'] = current_page.page(page_number)
    args['username'] =  auth.get_user(request).username
    return render(request, 'blog/index.html', args)


def post_in_detail(request, post_id):
    try:
        post = get_object_or_404(Post, pk=post_id)
    except Http404:
        return render(request, "blog/ERROR_404.html")
    args = {}
    args.update(csrf(request))
    args['post'] = post
    args['author'] = post.author
    args['category'] = post.category
    args['title'] = post.title
    args['img'] = post.img
    args['text'] = post.text
    args['date'] = post.published_date
    args['likes'] = post.likes
    args['comments'] = Comments.objects.filter(post__pk=post_id)
    if auth.get_user(request).username:
        #return HttpResponse(auth.get_user(request).username)
        comment_form = CommentForm
        args['comment_form'] = comment_form
    else:
        args['comment_form'] = None
    return render(request, "blog/detail.html", args)


def post_like(request, post_id):
    try:
        post = get_object_or_404(Post, pk=post_id)
    except Http404:
        return render(request, "blog/ERROR_404.html")


def add_comment(request, post_id):
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = Post.objects.get(id=post_id)
            comment.author = auth.get_user(request)
            form.save()
    return redirect('/'+post_id)

def new_post(request):
    args = {}
    args['page_title'] = "Напишите что-нибудь"
    args['post_form'] = NewPostForm
    if request.POST and auth.get_user(request).username:
        form = NewPostForm(request.POST)
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.author = auth.get_user(request)
            newpost.save()
            args["success"] = "Ваша запись успешно опубликована! Спасибо!"
        else:
            args['form_creation_error'] = "Введенные в форму данные не корректны."
    return render(request, "blog/new_post.html", args)
