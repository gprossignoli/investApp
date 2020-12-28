from django.apps import config
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.template import loader

from profiles.business.models import UserProfile
from profiles.presentation.forms import RegisterForm


def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})

    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.refresh_from_db()
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=new_user.username, password=raw_password)
            login(request, user)
            return redirect('user/{}'.format(user.id))


# TODO user id debe ser UUID para evitar identificadores contiguos
def user(request):
    return render(request, 'user_profile.html', {'user_name': 'prueba', 'user_risk_lvl': 1,
                                                 'risk_max_lvl': 6, 'min_risk_lvl': 1,
                                                 'index_growth': '../static/images/index_up.svg'})
