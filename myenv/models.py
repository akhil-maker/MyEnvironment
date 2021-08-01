from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    tagline = models.CharField(max_length=75)
    date = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='static', default="")
    follower = models.ManyToManyField(User, related_name='blog_posts', blank=True)

    def total_followers(self):
        return self.followers.count()

    def __str__(self):
        return str(self.title) + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')