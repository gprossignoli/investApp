from django.apps import config
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
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
            return redirect('user/{}'.format(user.id))

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


# TODO user id debe ser UUID para evitar identificadores contiguos
def user_profile(request):
    if request.method != 'GET':
        return HttpResponse(status=405)

    if request.user.is_authenticated:
        user = request.user
        return render(request, 'user_profile.html', {'user_name': user.username, 'user_risk_lvl': 1,
                                                     'risk_max_lvl': 6, 'min_risk_lvl': 1,
                                                     'index_growth': '../static/images/index_up.svg'})
    else:
        redirect('register')


