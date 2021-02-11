import datetime

from django.shortcuts import render, redirect

from investapp.forms import RiskProfileTestForm
from profiles.business.user_profile_service import UserProfileService


def index(request):
    return render(request, 'base.html', {})


def risk_profile(request):

    if request.method == "GET":
        form = RiskProfileTestForm()
        return render(request, 'risk_profile_test.html', {'form': form})

    elif request.method == "POST":
        form = RiskProfileTestForm(data=request.POST)
        if form.is_valid():

            if request.user.is_authenticated:
                UserProfileService().calculate_risk_level(scores=tuple([int(e) for e in form.cleaned_data.values()]),
                                                          username=request.user.username)
                return redirect("user_profile")

            else:
                risk_profile_calculated = UserProfileService() \
                    .calculate_risk_level(scores=tuple([int(e) for e in form.cleaned_data.values()]))
                return render(request, 'risk_profile_score.html', {'user_risk_lvl': risk_profile_calculated[0],
                                                                   'user_risk_score': risk_profile_calculated[1]})
