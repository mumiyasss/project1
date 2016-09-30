from django.contrib import admin
from .models import polls
from .models import answers

admin.site.register(polls)
admin.site.register(answers)