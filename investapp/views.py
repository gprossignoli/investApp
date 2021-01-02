import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    return render(request, 'base.html', {'time_stamp': datetime.datetime.today()})

