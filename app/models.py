from django.db import models

# Create your models here.
class ModelEgor(models.Model):
    name = models.TextField()
    password = models.TextField()