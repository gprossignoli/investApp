import pandas as pd

from django.db import models


class Symbol(models.Model):
    managed = False

    ticker = models.CharField(max_length=8)
    name = models.CharField(max_length=50)
    closures = pd.Series
    daily_returns = pd.Series
    first_date = models.DateField
    last_date = models.DateField


class Index(Symbol):
    pass


class Stock(Symbol):
    isin = models.CharField(max_length=8)
    dividends = pd.Series
    exchange = models.CharField(max_length=20)
