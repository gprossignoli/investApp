from django.shortcuts import render
from django.http import HttpResponseServerError, HttpResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

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
                'name': index['name'], 'ticker': index['ticker'],
                'last_price': index['last_price'], 'last_return': index['last_return']
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
            return render(request, "markets_indexes_list.html", context=context)


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
                'name': stock['name'], 'isin': stock['isin'], 'ticker': stock['ticker'],
                'last_price': stock['last_price']
            } for stock in stocks]
            paginator = Paginator(context_data, 6)

            n_page = request.GET.get('page', 1)
            try:
                stocks = paginator.page(n_page)
            except PageNotAnInteger:
                stocks = paginator.page(1)
            except EmptyPage:
                stocks = paginator.page(paginator.num_pages)

            context = {'stocks': stocks, 'has_next': stocks.has_next(), 'has_prev': stocks.has_previous(),
                       'exchange': exchange}
            return render(request, "markets_stocks_list.html", context=context)


def stock_detail(request, ticker):
    if request.method != 'GET':
        return HttpResponse(status=405)

    if request.method == 'GET':
        try:
            stock = MarketsService().get_symbol(ticker=ticker)
        except InternalServerError as e:
            return HttpResponseServerError()
        else:
            context = {'stock': stock, 'ticker': stock['ticker']}
            return render(request, "markets_stock_detail.html", context=context)


def index_detail(request, ticker):
    if request.method != 'GET':
        return HttpResponse(status=405)

    if request.method == 'GET':
        try:
            index = MarketsService().get_symbol(ticker=ticker)
        except InternalServerError as e:
            return HttpResponseServerError()
        else:
            context = {'index': index, 'ticker': index['ticker']}
            return render(request, "markets_index_detail.html", context=context)


class stock_detail_closures(BaseLineChartView):
    def get(self, request, *args, **kwargs):
        self._stock = MarketsService().get_symbol(ticker=request.GET['ticker'])
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


class symbol_detail_closures(BaseLineChartView):
    def get(self, request, *args, **kwargs):
        self._symbol = MarketsService().get_symbol(ticker=request.GET['ticker'])
        return super(symbol_detail_closures, self).get(request)

    def get_dataset_options(self, index, color):
        default_opt = super(symbol_detail_closures, self).get_dataset_options(index, color)
        default_opt['pointBorderWidth'] = '0.1'
        default_opt['pointRadius'] = '1.5'

        return default_opt

    def get_labels(self):
        return list(self._symbol['closures'].keys())

    def get_providers(self):
        return ['daily closes']

    def get_data(self):
        return [list(self._symbol['closures'].values())]


class symbol_detail_returns(BaseLineChartView):
    def get(self, request, *args, **kwargs):
        self._symbol = MarketsService().get_symbol(ticker=request.GET['ticker'])
        self._all_rets = [(round(float(v) * 100, 4), idx) if v != "null" else (0.0,idx) for idx, v
                          in self._symbol['daily_returns'].items()]
        return super(symbol_detail_returns, self).get(request)

    def get_datasets(self):
        datasets = []
        color_generator = [(0,128,0), (255,0,0)]
        data = self.get_data()
        providers = self.get_providers()
        num = len(providers)
        for i, entry in enumerate(data):
            color = color_generator[i]
            dataset = {"data": [abs(n) for n in entry]}
            dataset.update(self.get_dataset_options(i, color))
            if i < num:
                dataset["label"] = providers[i]  # series labels for Chart.js
                dataset["name"] = providers[i]
            datasets.append(dataset)
        return datasets

    def get_dataset_options(self, index, color):
        default_opt = super(symbol_detail_returns, self).get_dataset_options(index, color)

        return default_opt

    def get_labels(self):
        return list(self._symbol['daily_returns'].keys())[:1000]

    def get_providers(self):
        return ['positive returns', 'negative returns']

    def get_data(self):
        positives = []
        negatives = []
        for ret in self._all_rets:
            if ret[0] >= 0:
                positives.append(ret[0])
                negatives.append(0.0)
            else:
                negatives.append(ret[0])
                positives.append(0.0)

        return [positives[:1000], negatives[:1000]]
