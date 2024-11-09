from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))
# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(default='default=slug,')
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.RESTRICT)
    
    featured_image = CloudinaryField('image', default='placeholder')
    
    status = models.IntegerField(choices=STATUS, default=0)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    # This orders data from newest to oldest
    class Meta:
        ordering = ["created_on", "author"]
       
    def __str__(self):
        return f"{self.title} | written by {self.author}"







# This model will allow users to comment under the recipe

class Comment(models.Model):
    post = models.ForeignKey(Recipe, on_delete = models.CASCADE, related_name = "comment")
    body = models.TextField()
    
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'author')
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f" Comment {self.body} published by {self.author}"
