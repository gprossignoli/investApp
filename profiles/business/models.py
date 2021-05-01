
from django.contrib.auth.models import AbstractUser
from django.db import models

from investapp import settings as st


class UserProfile(AbstractUser):
    risk_level = models.IntegerField(default=st.RISK_PROFILE.BAJO.value)
    fav_index = models.CharField(default='^IBEX', max_length=20)

    def update_risk_level(self, risk_level: int):
        self.risk_level = risk_level
        self.save()

    def update_fav_index(self, index_ticker: str):
        self.fav_index = index_ticker
        self.save()
