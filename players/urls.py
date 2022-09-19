
from django.urls import path
from .views import *

urlpatterns = [
    path('getplayers', GetPlayers),
    path('addplayer', CreatePlayer),
    path('deleteplayer/<int:pk>', DeletePlayer),
    path('editplayer/<int:pk>', UpdatePlayer)
]