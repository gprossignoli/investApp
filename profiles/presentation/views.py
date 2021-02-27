import datetime

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import DeleteView, UpdateView

from profiles.business.models import UserProfile
from profiles.presentation.forms import RegisterForm
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
                next_view = request.session.get('view_after_login', 'user_profile')
                try:
                    del request.session['view_after_login']
                except KeyError:
                    pass
                return redirect(next_view)

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


class UserProfilePermissionsMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not self.user_has_permissions(request, kwargs['pk']):
            return self.handle_no_permission()

        return super(UserProfilePermissionsMixin, self).dispatch(request, *args, **kwargs)

    @staticmethod
    def user_has_permissions(request, requested_pk):
        return request.user.is_superuser or (request.user.pk == requested_pk)


class DeleteUserProfile(LoginRequiredMixin, UserProfilePermissionsMixin, DeleteView):
    model = UserProfile
    template_name = "user_profile_delete.html"

    success_url = "/"


class UpdateUserProfile(LoginRequiredMixin, UserProfilePermissionsMixin, UpdateView):
    model = UserProfile
    template_name = "user_profile_update.html"
    fields = ['username', 'email']
    success_url = "/profiles/user"

    def dispatch(self, request, *args, **kwargs):
        if request.method == "POST":
            if UserProfile.objects.filter(username=request.POST['username']).exists() and \
                    (UserProfile.objects.get_by_natural_key(username=request.POST['username']).pk is not kwargs['pk']):
                return self.handle_no_permission()
        return super(UpdateUserProfile, self).dispatch(request, *args, **kwargs)
