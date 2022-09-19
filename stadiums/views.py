from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Stadium

# Create your views here.
def CreateStadium(request):

    context = {}
    return render(request, 'stadiums/add_stadium.html', context)


def UpdateStadium(request):
    return

def DeleteStadium(request, pk):
    stadium = Stadium.objects.get(pk=pk)
    stadium.delete()
    return redirect('/')

def GetStadiums(request):
    players = Stadium.objects.all()
    
    return