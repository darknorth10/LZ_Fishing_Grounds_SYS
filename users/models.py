from django.db import models
from django.contrib.auth.models import AbstractUser

ROLE_CHOICES = [
  ("staff", "Staff"),
  ("admin", "Admin"),
  ("customer", "Customer"),
  ]
STATUS_CHOICES = [
  (1, "Active"),
  (0, "Inactive"),

  ]

class CustomUser(AbstractUser):
  role = models.CharField(max_length=10, choices=ROLE_CHOICES, null=True, default="customer")
  
  email = models.EmailField(unique=True)
  
  is_verified = models.BooleanField(default=False)
  
  is_active = models.BooleanField(default=True, choices=STATUS_CHOICES)
  
  def __str__(self):
    return self.username