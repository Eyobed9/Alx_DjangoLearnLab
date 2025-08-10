from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    profile_photo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    
    def __str__(self):
        return self.username
        
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()