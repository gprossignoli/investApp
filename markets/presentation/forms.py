import datetime

from django import forms
from django.core.exceptions import ValidationError

from markets.business.markets_service import MarketsService


class DateInput(forms.DateInput):
    input_type = 'date'


class InputAndChoice(object):
    def __init__(self, quantity_val, choice_val=''):
        self.quantity_val = quantity_val
        self.choice_val = choice_val


class InputAndChoiceWidget(forms.widgets.MultiWidget):
    def __init__(self, *args, **kwargs):
        my_choices = kwargs.pop("choices")
        widgets = (
            forms.TextInput(attrs={'min': '0', 'type': 'number', 'value': '0'}),
            forms.widgets.Select(choices=my_choices)
        )
        super(InputAndChoiceWidget, self).__init__(widgets, *args, **kwargs)

    def decompress(self, value):
        if value:
            return [value.quantity_val, value.choice_val]
        return [None, None]


class InputAndChoiceField(forms.MultiValueField):
    def __init__(self, *args, **kwargs):
        # you could also use some fn to return the choices;
        # the point is, they get set dynamically
        my_choices = kwargs.pop("choices", [("default", "default choice")])
        fields = (
            forms.fields.CharField(),
            forms.fields.ChoiceField(choices=my_choices),
        )
        super(InputAndChoiceField, self).__init__(fields, *args, **kwargs)
        # here's where the choices get set:
        self.widget = InputAndChoiceWidget(choices=my_choices)

    def compress(self, data_list):
        if data_list:
            if int(data_list[0]) > 0 and isinstance(data_list[1], str):
                return int(data_list[0]), data_list[1]
        return None, None


class PortfolioBuilderForm(forms.Form):
    stocks_tickers = []
    quantities = []
    indexes = [index['ticker'] for index in MarketsService().list_indexes()]

    for index in indexes:
        stocks_data = MarketsService().list_stocks(exchange=index)
        tickers = [(stock['ticker'],
                    '({stock_ticker}) {stock_name} - {index_ticker}'
                    .format(stock_ticker=stock['ticker'], stock_name=stock['name'], index_ticker=stock['exchange']))
                   for stock in stocks_data]
        stocks_tickers.extend(tickers)
        quantities.extend([(stock['ticker'], stock['ticker'])
                           for stock in stocks_data])

    stocks_1 = InputAndChoiceField(choices=stocks_tickers)
    stocks_2 = InputAndChoiceField(choices=stocks_tickers)
    stocks_3 = InputAndChoiceField(choices=stocks_tickers)
    stocks_4 = InputAndChoiceField(choices=stocks_tickers)
    stocks_5 = InputAndChoiceField(choices=stocks_tickers)

    first_date = forms.DateField(widget=DateInput)
    last_date = forms.DateField(widget=DateInput)

    stocks_1.label = 'Accion 1'
    stocks_2.label = 'Accion 2'
    stocks_3.label = 'Accion 3'
    stocks_4.label = 'Accion 4'
    stocks_5.label = 'Accion 5'
    first_date.label = 'Fecha Inicial'
    last_date.label = 'Fecha Final'

    class Meta:
        widgets = {'first_date': DateInput(), 'last_date': DateInput()}
        fields = ('stocks_select', 'first_date', 'last_date')

    def clean(self):
        cleaned_data = super(PortfolioBuilderForm, self).clean()

        validated_data = {}
        stock_1 = cleaned_data.get('stocks_1')
        stock_2 = cleaned_data.get('stocks_2')
        stock_3 = cleaned_data.get('stocks_3')
        stock_4 = cleaned_data.get('stocks_4')
        stock_5 = cleaned_data.get('stocks_5')
        stocks = 0
        stocks_tickers = set()
        validated_data['stocks'] = []
        if stock_1[0] is not None:
            validated_data['stocks'].append(stock_1)
            stocks += 1
            stocks_tickers.add(stock_1[1])
        if stock_2[0] is not None:
            validated_data['stocks'].append(stock_2)
            stocks += 1
            stocks_tickers.add(stock_2[1])
        if stock_3[0] is not None:
            validated_data['stocks'].append(stock_3)
            stocks += 1
            stocks_tickers.add(stock_3[1])

        if stock_4[0] is not None:
            validated_data['stocks'].append(stock_4)
            stocks += 1
            stocks_tickers.add(stock_4[1])

        if stock_5[0] is not None:
            validated_data['stocks'].append(stock_5)
            stocks += 1
            stocks_tickers.add(stock_5[1])

        if stocks < 2:
            self.add_error(None, ValidationError('Se necesita un minimo de dos simbolos seleccionados.'))
        if stocks != len(stocks_tickers):
            self.add_error(None, ValidationError('No se puede repetir acciones en la seleccion.'))
        last_date = cleaned_data['last_date']
        if last_date >= datetime.date.today():
            self.add_error(None, ValidationError('La última fecha no puede ser posterior a hoy.'))
        else:
            validated_data['last_date'] = last_date

        first_date = cleaned_data['first_date']
        if first_date >= last_date:
            self.add_error(None, ValidationError('La primera fecha debe ser anterior al último día'))
        else:
            validated_data['first_date'] = first_date

        return validated_data
