from django.contrib.auth.models import AbstractUser
from django.db import models

# Override Abstract user to make the email field unique.
# Note: overriding a default model requires a db drop and recreation
class User(AbstractUser):
  email = models.EmailField(unique=True)
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username']