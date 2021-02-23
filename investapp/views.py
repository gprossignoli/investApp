import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic.base import View

from investapp.forms import RiskProfileTestForm
from profiles.business.models import UserProfile
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
                request.session['risk_profile_calculated'] = risk_profile_calculated
                return redirect("risk_profile_score")


class RiskProfileScore(View):
    def get(self, request):
        try:
            risk_profile_calculated = request.session['risk_profile_calculated']
            del request.session['risk_profile_calculated']
        except Exception as e:
            raise e

        return render(request, 'risk_profile_score.html', {'user_risk_lvl': risk_profile_calculated[0],
                                                           'user_risk_score': risk_profile_calculated[1]})

    @login_required(login_url="profiles/login/")
    def post(self, request):
        user = UserProfile.objects.get_by_natural_key(username=request.user.username)
        user.update_risk_level(request.POST['risk_score'])
        redirect("user_profile")

