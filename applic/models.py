from django.db import models

from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(max_length=20)

class News(models.Model):
    title = models.CharField(max_length=60)
    matn = models.TextField()
    rasm = models.ImageField(upload_to="media/", null=True)
    created = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    bolim = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model):
    izoh = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name = "comments")
    created = models.DateTimeField(auto_now_add=True)
