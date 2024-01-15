from django.db import models
from django.contrib.auth.models import AbstractUser

ROLE_CHOICES = [
  ("staff", "Staff"),
  ("admin", "Admin"),
  ("customer", "Customer"),
  ]

class CustomUser(AbstractUser):
  role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="customer")
  email = models.EmailField(unique=True)
  is_verified = models.BooleanField(default=False)
  
  def __str__(self):
    return self.username