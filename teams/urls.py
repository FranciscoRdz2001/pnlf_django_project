
from django.urls import path
from .views import *

urlpatterns = [
    path('getstadiums', GetTeams),
    path('addteam', CreateTeam),
    path('deleteteam/<int:pk>', DeleteTeam),
    path('editteam/<int:pk>', UpdateTeam),
]