import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


from investapp.forms import RiskProfileTestForm
from profiles.business.models import UserProfile


def index(request):
    return render(request, 'base.html', {'time_stamp': datetime.datetime.today()})


def risk_profile(request):

    if request.method == "GET":
        form = RiskProfileTestForm()
        return render(request, 'risk_profile_test.html', {'time_stamp': datetime.datetime.today(),
                      'form': form})

    elif request.method == "POST":
        form = RiskProfileTestForm(data=request.POST)
        if form.is_valid():
            if request.user.is_authenticated():
                user = UserProfile.objects.get_by_natural_key(username=request.user.username)
                user.calculate_risk_level(scores=tuple([int(e) for e in form.cleaned_data.values()]))
                pass # TODO render profile
            else:
                pass # TODO render pagina de resultado perfil financiero.