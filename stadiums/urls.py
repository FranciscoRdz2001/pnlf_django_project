from django.urls import path
from . import views

urlpatterns = [
    path('stadiums', views.stadiums)
]