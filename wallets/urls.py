from django.urls import path
from . import views
urlpatterns=[path('',views.index,name='wallets_index')]
