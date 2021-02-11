from investapp import settings as st
from profiles.business.models import UserProfile


class UserProfileService:
    @staticmethod
    def calculate_risk_level(scores, username=None):
        """
        Calculates and updates the user profile (if the user is already authenticated)
        with the risk profile of the user from the answers of the test,
        associating the total score to one of the three risk levels established.

        NOTE: As the risk levels are fixed as business rule, the can be precalculated at the service start.

        :param scores: The scores of each question based on the answers of the user to the risk profile test.
        :type scores: tuple[int]
        :param username: Username of the user that has made the test if it was authenticated, otherwise is None.
        :type username: str

        :returns: The risk level calculated, with name and score.
        :rtype: tuple[str, float]
        """
        total_score = sum(scores)
        if total_score < st.GROUPS_LEFT_LIMITS.MODERADO.value:
            risk_level = st.RISK_PROFILE.BAJO
        elif total_score < st.GROUPS_LEFT_LIMITS.ALTO.value:
            risk_level = st.RISK_PROFILE.MODERADO
        else:
            risk_level = st.RISK_PROFILE.ALTO
        if username:
            user = UserProfile.objects.get_by_natural_key(username=username)
            user.update_risk_level(risk_level.value)

        return risk_level.name, total_score

