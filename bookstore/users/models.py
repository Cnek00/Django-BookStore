from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, verbose_name="E-posta")
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True, verbose_name="Profil Resmi")
    
    def __str__(self):
        return self.username
