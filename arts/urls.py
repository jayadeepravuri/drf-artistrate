from django.urls import path
from arts import views

urlpatterns = [
    path('arts/', views.ArtList.as_view()),
]