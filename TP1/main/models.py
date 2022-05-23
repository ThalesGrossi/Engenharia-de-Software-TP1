from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + "\n" + self.description

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likesc = models.ManyToManyField(User, related_name='comment_posts')

    def __str__(self):
        return '%s - %s' % (self.title, self.description)

    def get_absolute_url(self):
        return reverse("thread", kwargs={"pk": self.post_id})
    
    def total_likesc(self):
        return self.likesc.count()