from investapp import settings as st
from markets.business.models import Stock
from markets.infrastructure.data_access import DataReaderAbsFact
from utils.exceptions import ExternalResourceError, InternalServerError


class MarketsService:
    def __init__(self):
        self.symbols_dao = DataReaderAbsFact.get_instance().create_dao()

    def list_stocks(self):
        try:
            symbols = self.symbols_dao.get_all_stocks()
        except ExternalResourceError:
            raise InternalServerError(error="Error: external resource")
        stocks = []
        for symbol in symbols:
            stocks.append({
                'ticker': symbol['ticker'],
                'name': symbol['name'],
                'isin': symbol['isin']
            })
        return tuple(stocks)

    def list_indexes(self):
        try:
            symbols = self.symbols_dao.get_all_indexes()
        except ExternalResourceError:
            raise InternalServerError(error="Error: external resource")
        indexes = []
        for index in symbols:
            indexes.append({
                'ticker': index['ticker'],
                'name': index['name']
            })
        return tuple(indexes)

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

        return {'name': risk_level.name, 'value': risk_level.value}, total_score

