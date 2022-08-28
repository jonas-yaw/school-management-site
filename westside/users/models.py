from pyexpat import model
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    is_email_verified = models.BooleanField(default=False)
    token = models.TextField(blank=True, null=True)

