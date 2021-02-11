
from django.contrib.auth.models import AbstractUser
from django.db import models

from investapp import settings as st


class UserProfile(AbstractUser):
    risk_level = models.IntegerField(default=st.RISK_PROFILE.BAJO.value)

    def update_risk_level(self, risk_level: int):
        self.risk_level = risk_level
        self.save()
