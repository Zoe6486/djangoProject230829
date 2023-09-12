from django.contrib import admin

from blog.models import Category, Post, Profile, Comment

# Register your models here.
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Comment)