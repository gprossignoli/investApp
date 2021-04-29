from django.shortcuts import render
from django.http import HttpResponseServerError, HttpResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import TemplateView

from chartjs.views.lines import BaseLineChartView

from markets.business.markets_service import MarketsService
from utils.exceptions import InternalServerError


def list_indexes(request):
    if request.method != 'GET':
        return HttpResponse(status=405)

    if request.method == 'GET':
        try:
            indexes = MarketsService().list_indexes()
        except InternalServerError as e:
            if 'external resource' in e.error_msg:
                return HttpResponseServerError()
        else:
            context_data = [{
                'name': index['name'], 'ticker': index['ticker']
            } for index in indexes]
            paginator = Paginator(context_data, 6)

            n_page = request.GET.get('page', 1)
            try:
                indexes = paginator.page(n_page)
            except PageNotAnInteger:
                indexes = paginator.page(1)
            except EmptyPage:
                indexes = paginator.page(paginator.num_pages)

            context = {'indexes': indexes, 'has_next': indexes.has_next(), 'has_prev': indexes.has_previous()}
            return render(request, "markets_exchanges_list.html", context=context)


def list_stocks(request):
    if request.method != 'GET':
        return HttpResponse(status=405)

    if request.method == 'GET':
        exchange = request.GET.get('exchange')
        try:
            stocks = MarketsService().list_stocks(exchange=exchange)
        except InternalServerError as e:
            return HttpResponseServerError()
        else:
            context_data = [{
                'name': stocks['name'], 'isin': stocks['isin'], 'ticker': stocks['ticker']
            } for stocks in stocks]
            paginator = Paginator(context_data, 6)

            n_page = request.GET.get('page', 1)
            try:
                stocks = paginator.page(n_page)
            except PageNotAnInteger:
                stocks = paginator.page(1)
            except EmptyPage:
                stocks = paginator.page(paginator.num_pages)

            context = {'stocks': stocks, 'has_next': stocks.has_next(), 'has_prev': stocks.has_previous()}
            return render(request, "markets_stocks_list.html", context=context)


def stock_detail(request, ticker):
    if request.method != 'GET':
        return HttpResponse(status=405)

    if request.method == 'GET':
        try:
            stock = MarketsService().get_stock(ticker=ticker)
        except InternalServerError as e:
            return HttpResponseServerError()
        else:
            context = {'stock': stock, 'ticker': stock['ticker']}
            return render(request, "markets_stock_detail.html", context=context)


class stock_detail_closures(BaseLineChartView):
    def get(self, request, *args, **kwargs):
        self._stock = MarketsService().get_stock(ticker=request.GET['ticker'])
        return super(stock_detail_closures, self).get(request)

    def get_dataset_options(self, index, color):
        default_opt = super(stock_detail_closures, self).get_dataset_options(index, color)
        default_opt['pointBorderWidth'] = '0.1'
        default_opt['pointRadius'] = '1.5'

        return default_opt

    def get_labels(self):
        return list(self._stock['closures'].keys())

    def get_providers(self):
        return ['daily closes', 'dividends']

    def get_data(self):
        return [list(self._stock['closures'].values()), list(self._stock['dividends'].values())]


class stock_detail_returns(BaseLineChartView):
    def get(self, request, *args, **kwargs):
        self._stock = MarketsService().get_stock(ticker=request.GET['ticker'])
        return super(stock_detail_returns, self).get(request)

    def get_labels(self):
        return list(self._stock['closures'].keys())

    def get_providers(self):
        return ['daily returns']

    def get_data(self):
        return [[round(float(v) * 100, 4) if v != "null" else 0.0 for v in self._stock['daily_returns'].values()]]

    def get_dataset_options(self, index, color):
        default_opt = super(stock_detail_returns, self).get_dataset_options(index, color)
        default_opt['pointRadius'] = '0'
        return default_opt
