from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.text import slugify 


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

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Recipe, self).save(*args, **kwargs) 

    # This orders data from newest to oldest
    class Meta:
        ordering = ["created_on", "author"]
       
    def __str__(self):
        return f"{self.title} | written by {self.author}"



