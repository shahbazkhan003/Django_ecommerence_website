from django.db import models
from django.contrib.auth.models import AbstractUser

class UserRole(models.TextChoices):
    SELLER = 'Seller', 'Seller'
    MANAGER = 'Manager', 'Manager'
    BUYER = 'Buyer', 'Buyer'

class CustomUser(AbstractUser):
    role = models.CharField(
        max_length=20,
        choices=UserRole.choices,
        default=UserRole.BUYER 
    )

    def __str__(self):
        return self.username 


        
    