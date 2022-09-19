from django.shortcuts import render, redirect
from django.http import HttpResponse

from teams.forms import CreateTeamForm
from .models import Team

# Create your views here.
def CreateTeam(request):
    print(f'Create team endpoint by request method = {request.method} ')

    if request.method == 'POST':
        team = CreateTeamForm(request.POST)
        if team.is_valid():
            name = team.cleaned_data.get('name')
            trainer = team.cleaned_data.get('trainer')
            players_quantity = team.cleaned_data.get('players_quantity')
            stadium = team.cleaned_data.get('stadium')


            p, created = Team.objects.get_or_create(
                name= name,
                trainer = trainer,
                players_quantity = players_quantity,
            )
            p.save()
        return redirect('/')

    form = CreateTeamForm()
    context = {
        'action': 'create',
        'form': form
    }
    return render(request, 'teams/add_team.html', context)

def UpdateTeam(request, pk):
    t = Team.objects.get(pk=pk)

    if request.method == 'POST':
        team = CreateTeamForm(request.POST)
        print(team.is_valid())
        if team.is_valid():
            t.name = team.cleaned_data.get('name')
            t.trainer = team.cleaned_data.get('trainer')
            t.players_quantity = t.players_quantity
            t.stadium = team.cleaned_data.get('stadium')
            t.save()
        return redirect('/')

    form = CreateTeamForm(instance=t)
    context = {
        'action': 'edit',
        'form': form
    }
    return render(request, 'teams/add_team.html', context)

def DeleteTeam(request, pk):
    team = Team.objects.get(pk=pk)
    team.delete()
    return redirect('/')

def GetTeams(request):
    teams = Team.objects.all()
    return