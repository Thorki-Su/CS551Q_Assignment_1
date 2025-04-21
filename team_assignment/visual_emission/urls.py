from django.urls import path
from . import views

app_name = 'co2'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('country/<int:country_id>/', views.country_detail_view, name='country_detail'),
    path('group/<int:group_id>/', views.group_detail_view, name='group_detail'),
    path('api/country_emissions/<int:country_id>/', views.country_emissions_api, name='country_emissions_api'),
    path('feedback', views.feedback, name='feedback'),
    path('map', views.map, name='map'),
    path('export-chart/<int:country_id>/', views.export_country_chart_png, name='export_chart_png'),
    
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
]

handler404 = 'visual_emission.views.custom_404_view'
handler500 = 'visual_emission.views.custom_500_view'
