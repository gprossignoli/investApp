from django.urls import path

from profiles.presentation import views

urlpatterns = [
    path('register/', views.register, name='register_form'),
    path('user', views.user, name='user_profile'),
]
