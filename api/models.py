from django.db import models
from django.contrib.auth.models import User

class created_updated(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class BlogPost(created_updated):
    title = models.CharField(max_length=200, unique=True)
    subtitle = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(max_length=255, unique=True)
    image = models.ImageField(upload_to='blogs/', blank=True)
    body = models.TextField(blank=True, null=True)
    meta_description = models.CharField(max_length=150, blank=True)
    meta_keyword = models.CharField(max_length=150, blank=True)    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name='tags', blank=True)
    categorie = models.ForeignKey(Category, related_name='categories_post', on_delete=models.SET_NULL, null=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
