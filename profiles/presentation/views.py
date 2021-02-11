import datetime

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import DeleteView

from profiles.business.models import UserProfile
from profiles.presentation.forms import RegisterForm
from profiles.business.user_profile_service import UserProfileService
from investapp import settings as st


def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})

    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.refresh_from_db()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=new_user.username, password=raw_password)
            login(request, user)
            return redirect('user_profile')

        return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == "GET":
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

    elif request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('user_profile')

        return render(request, 'login.html', {'form': form})


def user_profile(request):
    if request.method != 'GET':
        return HttpResponse(status=405)

    if not request.user.is_authenticated:
        return redirect('user_login')

    if request.method == 'GET':
        user = request.user
        return render(request, 'user_profile.html', {'user_name': user.username,
                                                     'user_risk_lvl': st.RISK_PROFILE(user.risk_level).name,
                                                     'user_info': user,
                                                     'risk_max_lvl': st.RISK_MAX_LVL,
                                                     'min_risk_lvl': st.RISK_MIN_LVL,
                                                     'index_growth': True, 'index_value': 0.54,
                                                     'index_last_value': 8000, 'index_points_value': 0.94})
    elif request.method == 'PUT':
        pass


def user_logout(request):
    logout(request)
    return redirect("index")


class DeleteUserProfile(DeleteView):
    model = UserProfile
    template_name = "user_profile_delete.html"

    success_url = "/"
