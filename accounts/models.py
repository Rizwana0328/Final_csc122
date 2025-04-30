from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser 
from django.conf import settings
from django.db import models


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)

