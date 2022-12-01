from django.db import models

# Create your models here.
class Signup(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    username = models.CharField(unique=True, max_length=150)
    password1 = models.CharField(max_length=128)
    password2 = models.CharField(max_length=128)
    class Meta:
        db_table = "smile"