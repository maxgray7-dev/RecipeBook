from django.db import models
from cloudinary.models import CloudinaryField



# Create your models here.

class MyPage(models.Model):
    name = models.CharField(max_length = 25)
    profile_image = CloudinaryField('image', default='placeholder')
    content = models.TextField(max_length=500)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
