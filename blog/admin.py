from django.contrib import admin
from .models import User, Post, Comment, Profile, Gender

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Profile)
admin.site.register(Gender)