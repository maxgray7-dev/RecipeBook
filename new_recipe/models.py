from django.db import models
from cloudinary.models import CloudinaryField



# Create your models here.

class NewRecipeRequest(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField()
    name = models.CharField(max_length=25) 
    featured_image = CloudinaryField('image', default='placeholder')
    status = models.IntegerField()

    def __str__(self):
        return f"Thank you for sharing the recipe of {self.title} with us!"