from django.urls import path
from . import views

urlpatterns = [
    path('get_weather_data_successful', views.send_request),
    path('get_weather_data_unsuccessful', views.send_request_fail)
]