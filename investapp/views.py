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
            risk_profile_calculated = UserProfileService() \
                .calculate_risk_level(scores=tuple([int(e) for e in form.cleaned_data.values()]))
            request.session['risk_profile_calculated'] = risk_profile_calculated
            return redirect("risk_profile_score")


class RiskProfileScore(View):
    def get(self, request):
        risk_profile_calculated = request.session['risk_profile_calculated']
        return render(request, 'risk_profile_score.html', {'user_risk_lvl': risk_profile_calculated[0]['name'],
                                                           'user_risk_score': risk_profile_calculated[1]})

    def post(self, request):
        if not request.user.is_authenticated:
            request.session['view_after_login'] = 'risk_profile_score'
            return redirect("user_login")

        user = UserProfile.objects.get_by_natural_key(username=request.user.username)
        user.update_risk_level(request.session['risk_profile_calculated'][0]['value'])
        return redirect("user_profile")
