from __future__ import annotations
from abc import ABC, abstractmethod

import ujson

from utils.exceptions import ExternalResourceError
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
        url = self.base_url.join([st.FINCALCS_SYMBOLS_ENDPOINT, '/{}'.format(ticker)])
        try:
            symbol = ujson.loads(HttpRequest(status_forcelist=[400, 404, 500]).get(url))
        except HttpRequestException:
            pass
            # TODO exception?
        else:
            return symbol
