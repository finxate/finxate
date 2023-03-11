from django.urls import path
from . import views

app_name = 'transactions'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_transaction, name='add_transaction'),
    path('list/', views.transactions_list, name='transactions_list'),
]
