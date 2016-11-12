from django.shortcuts import render
from .models import Post
# Create your views here.

def index_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts' : posts} )