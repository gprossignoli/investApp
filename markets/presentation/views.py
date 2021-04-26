from django.shortcuts import render
from django.http import HttpResponseServerError
from django.views import generic

from markets.business.markets_service import MarketsService
from markets.business.models import Stock, Index
from investapp import settings as st
from utils.exceptions import InternalServerError


class IndexListView(generic.ListView):
    model = Index
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        try:
            indexes = MarketsService().list_indexes()
        except InternalServerError as e:
            if 'external resource' in e.error_msg:
                return HttpResponseServerError()
        else:
            context_data = [{
                'name': index['name'], 'ticker': index['ticker']
            } for index in indexes]

            context = {'indexes': context_data}
            return render(request, "markets_exchanges_list.html", context=context)


class StocksListView(generic.ListView):
    model = Stock
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        try:
            stocks = MarketsService().list_stocks()
        except InternalServerError as e:
            return HttpResponseServerError()
        else:
            context_data = [{
                'name': stock.name, 'isin': stock.isin, 'ticker': stock.ticker,
                'last_date': stock.last_date.strftime("%d-%m-%Y"), 'last_price': stock.closures[-1]} for stock in stocks]

            context = context_data

            return render(request, "markets_stocks_list.html", context=context)
