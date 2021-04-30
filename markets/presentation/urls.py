from django.urls import path

from markets.presentation import views

urlpatterns = [
    path('', views.list_indexes, name='indexes'),
    path('stocks/', views.list_stocks, name='stocks'),
    path('stocks/<str:ticker>/', views.stock_detail, name='stock'),
    path('stocks/closures', views.stock_detail_closures.as_view(), name='stock_closures'),
    path('stocks/returns', views.symbol_detail_returns.as_view(), name='stock_returns'),
    path('indexes/', views.list_indexes, name='indexes'),
    path('indexes/<str:ticker>/', views.index_detail, name='index'),
    path('indexes/closures', views.symbol_detail_closures.as_view(), name='index_closures'),
    path('indexes/returns', views.symbol_detail_returns.as_view(), name='index_returns'),
]
