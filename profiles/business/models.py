from django.contrib.auth.models import AbstractUser
from django.db import models


class UserProfile(AbstractUser):
    risk_level = models.IntegerField(default=1)


