from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    age  = models.DateTimeField( blank=True,null=True)
    gender = models.ForeignKey('blog.Gender', on_delete=models.PROTECT)

class Gender(models.Model):
    gender = models.CharField(max_length=15)
    def __str__(self):
        return self.gender
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey('blog.Profile', on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    content = models.CharField(max_length=10000)
    create_date = models.DateTimeField(default=timezone.now())
    published_data = models.DateTimeField(blank=True, null=True)
    def publish(self):
        self.published_data = timezone.now()
        self.save()
    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.CharField(max_length=128)
    post = models.ForeignKey('blog.Post',on_delete=models.CASCADE, related_name="comments")
    content = models.CharField(max_length=800)
    create_date = models.DateTimeField(default=timezone.now())

