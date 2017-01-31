

from django.db import models
from PIL import Image
from django.conf import settings
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
import datetime

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='images/',default='Images/None/No-img.jpg')
    published = models.DateTimeField(blank=True, null=True)
    subscibers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='subscribers', blank=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='likes', blank=True)
    subscribe = models.EmailField()
    draft = models.BooleanField(default=False)
    updated_date = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE, null=True)
    highlighted = models.TextField()

    class Meta:
    	ordering = ['published','updated_date']
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.Foreignkey(Post, editable=False,related_name='comments')
    author = models.CharField(max_length=100)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='likes', blank=True)

    class Meta:
        unique_together = ('post')

    def __str__(self):
        return self.author






