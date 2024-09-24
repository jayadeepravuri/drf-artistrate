from django.urls import path
from geolocation import views


urlpatterns = [
    path('geolocations/', views.GeolocationList.as_view()),
    path('geolocations/<int:pk>/', views.GeolocationDetail.as_view()),
]