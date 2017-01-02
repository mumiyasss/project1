from django.contrib import admin
from .models import Post
from .models import Category
from .models import Comments
from .models import Likes

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comments)
admin.site.register(Likes)

