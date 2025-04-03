from django.urls import path
from . import views

app_name = 'co2'

urlpatterns = [
    path('', views.homepage, name='homepage'),
]