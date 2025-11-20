from django.urls import path
from .views import stk_push
urlpatterns=[path('mpesa/stk_push/', stk_push, name='mpesa_stk_push')]
