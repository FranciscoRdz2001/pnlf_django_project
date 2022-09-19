from django.urls import path
from .views import *

urlpatterns = [
    path('getstadiums', GetStadiums),
    path('addstadium', CreateStadium),
    path('deletestadium/<int:pk>', DeleteStadium),
    path('editstadium/<int:pk>', UpdateStadium),
]