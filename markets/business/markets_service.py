import numpy as np

from markets.infrastructure.data_access import DataReaderAbsFact
from utils.exceptions import ExternalResourceError, InternalServerError


class MarketsService:
    def __init__(self):
        self.symbols_dao = DataReaderAbsFact.get_instance().create_dao()

    def list_stocks(self, exchange: str = None):
        try:
            symbols = self.symbols_dao.get_all_stocks()
        except ExternalResourceError:
            raise InternalServerError(error="Error: external resource")
        stocks = []
        for symbol in symbols:
            if symbol['exchange'] == exchange:
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

    def get_stock(self, ticker):
        try:
            stock_data = self.symbols_dao.get_symbol(ticker)
            stock_data['daily_returns'] = self.__clean_returns(stock_data['daily_returns'])

        except ExternalResourceError:
            raise InternalServerError(error="Error: external resource")

        return stock_data

    @staticmethod
    def __clean_returns(returns):
        """
        Cleans extreme outliers to maintain a good visualization.
        """
        rets = {k: round(float(v), 4) if v != "null" else 0.0 for k,v in returns.items()}
        std = np.array(list(rets.values())).std()
        avg = sum(list(rets.values())) / len(rets.values())
        for k, ret in rets.items():
            if abs(avg - ret) >= 2 * std:
                if ret < 0:
                    v = avg - (2 * std)
                else:
                    v = avg + (2 * std)
            else:
                v = rets[k]
            rets[k] = str(v)

        return rets
