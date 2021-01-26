
from django.contrib.auth.models import AbstractUser
from django.db import models

from investapp import settings as st


class UserProfile(AbstractUser):
    risk_level = models.IntegerField(default=st.RISK_PROFILE.BAJO.value)

    def calculate_risk_level(self, scores):
        """
        Calculates and updates the user profile with the risk profile of the user from the answers of the test,
        associating the total score to one of the three risk levels established.

        NOTE: As the risk levels are fixed as business rule, the can be precalculated at the service start.

        :param scores: The scores of each question based on the answers of the user to the risk profile test.
        :type scores: tuple[int]
        """
        total_score = sum(scores)
        if total_score < st.GROUPS_LEFT_LIMITS.MODERADO:
            self.risk_profile = st.RISK_PROFILE.BAJO
        elif total_score < st.GROUPS_LEFT_LIMITS.ALTO:
            self.risk_profile = st.RISK_PROFILE.MODERADO
        else:
            self.risk_profile = st.RISK_PROFILE.ALTO
        self.save()
