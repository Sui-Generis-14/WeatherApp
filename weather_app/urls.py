from django.urls import path
from . import views

app_name = 'weather_app'

urlpatterns = [
    # Main pages
    path('', views.index, name='index'),
    
    # API endpoints
    path('api/weather/', views.api_weather, name='api_weather'),
    path('api/weather/coordinates/', views.api_weather_by_coordinates, name='api_weather_by_coordinates'),
    
    # CRUD operations for weather records
    path('records/', views.weather_records_list, name='weather_records_list'),
    path('records/create/', views.weather_record_create, name='weather_record_create'),
    path('records/<int:pk>/', views.weather_record_detail, name='weather_record_detail'),
    path('records/<int:pk>/update/', views.weather_record_update, name='weather_record_update'),
    path('records/<int:pk>/delete/', views.weather_record_delete, name='weather_record_delete'),
    
    # Data export
    path('export/<str:format_type>/', views.export_data, name='export_data'),
]
