from django.urls import path
from . import views

app_name = 'co2'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('country/<int:country_id>/', views.country_detail_view, name='country_detail'),
    path('group/<int:group_id>/', views.group_detail_view, name='group_detail'),
]