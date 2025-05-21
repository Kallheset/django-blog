from django.db import models
from django.db.models.fields.files import ImageField
from django.db.models.fields import CharField, URLField

# Create your models here.


class Project(models.Model):
    title = CharField(max_length=200)
    description = CharField(max_length=250)
    image = ImageField(upload_to="porfolio/images/")
    url = URLField(blank=True)
    github_url = URLField(blank=True)

    def __str__(self):
        return self.title
