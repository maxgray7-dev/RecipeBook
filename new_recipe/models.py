from django.db import models
from django.utils import timezone
from cloudinary.models import CloudinaryField




# Create your models here.

class Recipe(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.CharField(max_length=25, default='') 
    featured_image = CloudinaryField('image', default='placeholder')
    date_posted=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Thank you for sharing the recipe of {self.title} with us!"