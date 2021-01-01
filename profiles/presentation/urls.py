from django.urls import path

from profiles.presentation import views

urlpatterns = [
    path('register/', views.register, name='register_form'),
    path('login/', views.user_login, name='user_login'),
    path('user', views.user_profile, name='user_profile'),
]
