from django.shortcuts import render, get_object_or_404
from .models import Post, Comments
from django.contrib import auth
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
    except Post.DoesNotExist:
        raise render(request, "blog/404_ERROR.html")
    args = {}
    args['author'] = post.author
    args['category'] = post.category
    args['title'] = post.title
    args['text'] = post.text
    args['date'] = post.published_date
    args['comments'] = Comments.objects.filter(post__pk=post_id)
    return render(request, "blog/detail.html", args)