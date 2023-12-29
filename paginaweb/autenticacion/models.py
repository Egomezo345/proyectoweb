from django.db import models
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cui = models.IntegerField()
    profile_imagen = models.ImageField(upload_to='profile_images/', null=True, blank=True)

# Create your models here.
