from django.shortcuts import render, get_object_or_404, Http404, redirect, HttpResponse
from .models import Post, Comments, Likes
from django.contrib import auth
from .forms import CommentForm, NewPostForm
from django.views.decorators.csrf import csrf_protect
from django.core.paginator import Paginator
from . import messages
import os


def index_list(request, page_number=1):
    posts = Post.objects.all().order_by('-id')
    current_page = Paginator(posts, 2)
    args = {}
    args['posts'] = current_page.page(page_number)
    args['username'] =  auth.get_user(request).username
    return render(request, 'blog/index/main.html', args)

@csrf_protect
def post_in_detail(request, post_id):
    try:
        post = get_object_or_404(Post, pk=post_id)
        likes = Likes.objects.filter(post=post)
    except Http404:
        return render(request, "ERROR_404.html")
    args = {}
    #args.update(csrf(request))
    args['user'] = auth.get_user(request)
    args['post'] = post
    args['author'] = post.author
    args['category'] = post.category
    args['title'] = post.title
    args['img'] = post.img
    args['text'] = post.text
    args['date'] = post.published_date
    args['likes'] = likes
    args['comments'] = Comments.objects.filter(post__pk=post_id)
    if auth.get_user(request).username:
        comment_form = CommentForm
        args['comment_form'] = comment_form
    else:
        args['comment_form'] = None
    return render(request, "blog/detail/main.html", args)


def post_like(request, post_id):
    if auth.get_user(request):
        this_post = Post.objects.get(pk=post_id)
        # Если лайк уже существует...
        if Likes.objects.filter(post=this_post, user=auth.get_user(request)):
            like = Likes.objects.filter(post=this_post, user=auth.get_user(request))
            like.delete()
        else: # Если лайка не было...
            like = Likes(post=this_post, user=auth.get_user(request))
            like.save()
    return redirect('/'+post_id)


def delete_comment(request, comment_id, post_id):
    this_comment = Comments.objects.get(id=comment_id)
    this_user = auth.get_user(request)
    if this_user.username:
        if this_comment:
            if this_comment.author == this_user:
                this_comment.delete()
    return redirect('/'+post_id)


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
    if not auth.get_user(request).username:
        return render(request, "ERROR_PERMISSION.html")
    args = {}
    args['page_title'] = messages.newPostPageTitle
    args['post_form'] = NewPostForm
    if request.POST and auth.get_user(request).username:
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.author = auth.get_user(request)
            newpost.save()
            args["success"] = messages.newPostSuccess
        else:
            args['form_creation_error'] = messages.newPostFormCreationError
    return render(request, "blog/new_post/main.html", args)
