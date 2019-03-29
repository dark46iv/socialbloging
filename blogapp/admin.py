from django.contrib import admin
from .models import Post, PostInstance

# Register your models here.

admin.site.register(Post)
admin.site.register(PostInstance)