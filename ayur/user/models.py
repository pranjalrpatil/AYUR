from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_no=models.CharField(max_length=10)
    def __str__(self) -> str:
        return str(self.first_name)

