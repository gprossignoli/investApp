from __future__ import annotations
from abc import ABC, abstractmethod

import ujson

from utils.exceptions import ExternalResourceError, SymbolNotFoundError
from utils.http_request import HttpRequest, HttpRequestException
from investapp import settings as st


class DataReaderAbsFact(ABC):
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = FincalcsDataReaderFact()
        return cls.instance

    @abstractmethod
    def create_dao(self) -> AbstractDao:
        pass


class FincalcsDataReaderFact(DataReaderAbsFact):
    def create_dao(self) -> AbstractDao:
        return FincalcsDao()


class AbstractDao(ABC):
    @abstractmethod
    def connect_to_data_source(self):
        pass


class FincalcsDao(AbstractDao):
    def __init__(self):
        self.base_url = self.connect_to_data_source()

    def connect_to_data_source(self):
        return st.FINCALCS_HOST

    def get_all_stocks(self):
        url = self.base_url + st.FINCALCS_SYMBOLS_ENDPOINT + '/stocks'
        try:
            symbols = ujson.loads(HttpRequest(status_forcelist=[400, 404, 500]).get(url).content)
        except HttpRequestException as e:
            st.logger.exception(e)
            raise ExternalResourceError()
        else:
            return symbols

    def get_all_indexes(self):
        url = self.base_url + st.FINCALCS_SYMBOLS_ENDPOINT + '/indexes'
        try:
            indexes = ujson.loads(HttpRequest(status_forcelist=[400, 404, 500]).get(url).content)
        except HttpRequestException as e:
            st.logger.exception(e)
            raise ExternalResourceError()
        else:
            return indexes

    def get_symbol(self, ticker: str):
        url = self.base_url + st.FINCALCS_SYMBOLS_ENDPOINT + '/{}'.format(ticker)

        try:
            resp = HttpRequest(status_forcelist=[400, 500]).get(url)
            if resp.status_code == 404:
                raise SymbolNotFoundError()
            symbol = ujson.loads(resp.content)
        except HttpRequestException as e:
            st.logger.exception(e)
            raise ExternalResourceError()
        else:
            return symbol

    def get_portfolio(self, stocks, shares_per_stock, first_date_data, last_date_data):
        url = self.base_url + st.FINCALCS_PORTFOLIO_ENDPOINT
        try:
            tickers = ','.join(stocks)
            sps = ['{}:{}'.format(k,v) for k,v in shares_per_stock.items()]
            sps = ','.join(sps)
            body = {'tickers': tickers, 'sharesPerStock': sps, 'initial_date': first_date_data,
                    'end_date': last_date_data}
            resp = HttpRequest(status_forcelist=[400, 500]).post(url, body=body)
            if resp.status_code == 404:
                raise SymbolNotFoundError()
            portfolio = ujson.loads(resp.content)
        except HttpRequestException as e:
            st.logger.exception(e)
            raise ExternalResourceError()
        else:
            return portfolio
