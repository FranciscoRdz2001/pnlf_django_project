from django.http import HttpResponse
from django.shortcuts import render
from .models import Player


# Create your views here.
def CreatePlayer(request):
    return
    
def UpdatePlayer(request):
    return
    
def DeletePlayer(request):
    return
    
def GetPlayers(request):
    players = Player.objects.all()
    message = 'No players in list' if len(players) == 0 else 'Has players'

    return HttpResponse(message)
    