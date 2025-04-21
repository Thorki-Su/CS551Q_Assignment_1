from django.urls import path
from . import views

app_name = 'co2'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('country/<int:country_id>/', views.country_detail_view, name='country_detail'),
    path('group/<int:group_id>/', views.group_detail_view, name='group_detail'),
    path('api/country_emissions/<int:country_id>/', views.country_emissions_api, name='country_emissions_api'),
    path('feedback', views.feedback, name='feedback'),
    path('export-chart/<int:country_id>/', views.export_country_chart_png, name='export_chart_png'),
]

handler404 = 'visual_emission.views.custom_404_view'
handler500 = 'visual_emission.views.custom_500_view' #error handlers for 404 and 500