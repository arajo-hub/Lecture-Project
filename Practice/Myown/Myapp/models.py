from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class user(models.Model):
    first_name=models.CharField(max_length=128)
    last_name=models.CharField(max_length=128)
    e_mail=models.EmailField(max_length=264, unique=True)

class UserProfileInfo(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    portfolio_site=models.URLField(blank=True)
    profile_pic=models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username
