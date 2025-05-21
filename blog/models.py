from django.db import models
from datetime import datetime

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='blog/images/')
    date = models.DateField(datetime.now, blank=True)
    
    
    def __str__(self):
        return self.title