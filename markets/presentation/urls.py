from django.urls import path

from markets.presentation import views

urlpatterns = [
    path('stocks/', views.list_stocks, name='stocks'),
    path('', views.list_indexes, name='indexes'),
]
