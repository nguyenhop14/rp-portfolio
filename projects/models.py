from django.db import models

# Create your models here.
from django.db import models
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path='/img')


class Dev(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)