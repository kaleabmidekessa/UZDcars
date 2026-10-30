from django.urls import path
from .views import homepage

app_name = 'clientlists'

urlpatterns = [
    path('',homepage,name = '')
    ]