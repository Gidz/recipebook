from django.db import models
from django.contrib.auth.models import AbstractUser 

class User(AbstractUser):
    """
    Extending the default User model to add more fields.
    """
    first_name = models.CharField(max_length=30) 
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length = 50, unique=True)

