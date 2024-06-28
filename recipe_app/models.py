from django.db import models
from django.contrib.auth.models import User


STATUS = ((0, "Draft"), (1, "Published"))
# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.RESTRICT)
    
    featured_image = CloudinaryField('image', default='placeholder')
    
    status = models.IntegerField(choices=STATUS, default=0)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on", "author"]
    
    
    
    def __str__(self):
        return f"{self.title} | written by {self.author}"