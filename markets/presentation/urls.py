from django.urls import path

from markets.presentation import views
from markets.presentation.views import line_chart, line_chart_json

urlpatterns = [
    path('', views.list_indexes, name='indexes'),
    path('stocks/', views.list_stocks, name='stocks'),
    path('stocks/<str:ticker>/', views.stock_detail, name='stock'),
    path('stocks/closures', views.stock_detail_closures.as_view(), name='stock_closures'),
    path('stocks/returns', views.stock_detail_returns.as_view(), name='stock_returns'),
    path('chart', line_chart, name='line_chart'),
    path('chartJSON', line_chart_json, name='line_chart_json'),
]
