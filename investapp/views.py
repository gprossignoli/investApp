import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from investapp.forms import RiskProfileTestForm


def index(request):
    return render(request, 'base.html', {'time_stamp': datetime.datetime.today()})


def risk_profile(request):
    user_already_logged = False
    if request.user.is_authenticated:
        user_already_logged = True

    if request.method == "GET":
        form = RiskProfileTestForm()
        return render(request, 'risk_profile_test.html', {'time_stamp': datetime.datetime.today(),
                      'form': form, 'user_already_logged': user_already_logged})
