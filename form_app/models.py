from django.db import models

# Create your models here.

class User (models.Model):
    name = models.CharField(max_length=25)
    height = models.IntegerField()
    weight = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)