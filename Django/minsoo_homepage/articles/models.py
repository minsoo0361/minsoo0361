from django.db import models

# Create your models here.
class Article(models.Model):
    name = models.CharField(max_length = 10)
    content = models.TextField()