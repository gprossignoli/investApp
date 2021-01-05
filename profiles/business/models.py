from django.contrib.auth.models import AbstractUser
from django.db import models

from investapp import settings as st


class UserProfile(AbstractUser):
    risk_level = models.IntegerField(default=st.RISK_PROFILE.BAJO.value)


