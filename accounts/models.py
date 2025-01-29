from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from .managers import CustomUserManager

class CustomUser(AbstractBaseUser):

    class Roles(models.TextChoices):
        SELLER = "Seller", "Seller"
        MANAGER = "Manager", "Manager"
        BUYER = "Buyer", "Buyer"

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    role = models.CharField(max_length=50,choices=Roles.choices,default=Roles.BUYER)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name","role"]

