from django.shortcuts import render
from django.http import HttpResponseServerError, HttpResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

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


"""class StocksListView(generic.ListView):
    model = Stock
    paginate_by = 1

    def get(self, request, *args, **kwargs):
        exchange = request.GET.get('exchange')
        try:
            stocks = MarketsService().list_stocks(exchange=exchange)
        except InternalServerError as e:
            return HttpResponseServerError()
        else:
            context_data = [{
                'name': stock['name'], 'isin': stock['isin'], 'ticker': stock['ticker']} for stock in stocks]

            context = {'stocks': context_data}

            return render(request, "markets_stocks_list.html", context=context)
"""