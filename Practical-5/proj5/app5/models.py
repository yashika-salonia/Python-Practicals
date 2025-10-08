from django.db import models
from taggit.managers import TaggableManager
from django.utils.timezone import now
from django.contrib.auth.models import User

class Post(models.Model):
    postid=models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    author=models.CharField(max_length=100)
    timestamp = models.DateTimeField(default=now, blank=True)
    postauthor = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = TaggableManager()
    category=models.CharField(max_length=100)
    slug=models.SlugField(unique=True)
