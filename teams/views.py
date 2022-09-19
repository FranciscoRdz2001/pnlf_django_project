from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Team

# Create your views here.
def CreateTeam(request):
    
    context = {}
    return render(request, 'teams/add_team.html', context)

def UpdateTeam(request):
    return

def DeleteTeam(request, pk):
    team = Team.objects.get(pk=pk)
    team.delete()
    return redirect('/')

def GetTeams(request):
    teams = Team.objects.all()
    return