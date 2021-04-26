from django.urls import path

from markets.presentation import views

urlpatterns = [
    path('stocks/', views.StocksListView.as_view(), name='stocks'),
    path('', views.IndexListView.as_view(), name='indexes'),
]
