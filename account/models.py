from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    nid = models.CharField(max_length=13, unique=True)
    balance = models.DecimalField(decimal_places=2, max_digits=12, default=0)