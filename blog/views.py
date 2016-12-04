from django.shortcuts import render, get_object_or_404, Http404, redirect, HttpResponse
from .models import Post, Comments
from django.contrib import auth
from .forms import CommentForm
from django.core.context_processors import csrf

# Create your views here.


def index_list(request):
    posts = Post.objects.all()
    args = {}
    args['posts'] = posts
    args['username'] =  auth.get_user(request).username
    return render(request, 'blog/index.html', args)


def post_in_detail(request, post_id):
    try:
        post = get_object_or_404(Post, pk=post_id)
    except Http404:
        return render(request, "blog/404_ERROR.html")
    args = {}
    args.update(csrf(request))
    args['post'] = post
    args['author'] = post.author
    args['category'] = post.category
    args['title'] = post.title
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
        return render(request, "blog/404_ERROR.html")


def add_comment(request, post_id):
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = Post.objects.get(id=post_id)
            comment.author = auth.get_user(request)
            form.save()
    return redirect('/'+post_id)

