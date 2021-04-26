from django.urls import path

from markets.presentation import views

urlpatterns = [
    path('stocks/', views.StocksListView.as_view(), name='stocks'),
    path('', views.list_indexes, name='indexes'),
]
