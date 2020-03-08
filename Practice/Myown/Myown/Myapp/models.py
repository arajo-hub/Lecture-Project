from django.db import models

# Create your models here.
class user(models.Model):
    first_name=models.CharField(max_length=128)
    last_name=models.CharField(max_length=128)
    e_mail=models.EmailField(max_length=264, unique=True)
