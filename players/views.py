from queue import Empty
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Player
from teams.models import Team
from .forms import CreatePlayerForm

# Create your views here.
def CreatePlayer(request):
    print(f'Create player endpoint by request method = {request.method} ')

    if request.method == 'POST':
        player = CreatePlayerForm(request.POST)
        if player.is_valid():
            name = player.cleaned_data.get('name')
            age = player.cleaned_data.get('age')
            number = player.cleaned_data.get('number')
            nationality = player.cleaned_data.get('nationality')
            shirt_number = player.cleaned_data.get('shirt_number')
            team = player.cleaned_data.get('team')

            if team is not None:
                t = Team.objects.get(pk=team.pk)
                t.players_quantity = 1 if t.players_quantity is None else t.players_quantity + 1
                t.save()


            p, created = Player.objects.get_or_create(
                name = name,
                age = age,
                number = number,
                nationality = nationality,
                shirt_number = shirt_number,
                team = team
            )
            p.save()
        return redirect('/')

    form = CreatePlayerForm()
    context = {
        'action': 'create',
        'form': form
    }
    return render(request, 'player/add_player.html', context)
    
def UpdatePlayer(request, pk):

    p = Player.objects.get(pk=pk)

    if request.method == 'POST':
        player = CreatePlayerForm(request.POST)

        if player.is_valid():

            # Check if has a team
            oldTeamID = None
            if p.team is not None:
                oldTeamID = p.team.id
                if player.cleaned_data.get('team') is None or p.team.id != player.cleaned_data.get('team').id:
                    t = Team.objects.get(pk=p.team.id)
                    t.players_quantity -= 1
                    t.save()
                    print(t.players_quantity)


            p.name = player.cleaned_data.get('name')
            p.age = player.cleaned_data.get('age')
            p.number = player.cleaned_data.get('number')
            p.nationality = player.cleaned_data.get('nationality')
            p.shirt_number = player.cleaned_data.get('shirt_number')
            p.team = player.cleaned_data.get('team')

            if p.team is not None and (oldTeamID is None or oldTeamID != p.team.id):
                t = Team.objects.get(pk=p.team.pk)

                t.players_quantity = 1 if t.players_quantity is None else t.players_quantity + 1
                t.save()
                print(t.players_quantity)

            p.save()
        return redirect('/')

    form = CreatePlayerForm(instance=p)
    context = {
        'action': 'edit',
        'form': form
    }
    return render(request, 'player/add_player.html', context)
    
def DeletePlayer(request, pk):
    player = Player.objects.get(pk=pk)

    if player.team is not None:
        t = Team.objects.get(pk=player.team.id)
        t.players_quantity -= 1
        t.save()

    print(f'Delete method {player.id} ')
    player.delete()
    return redirect('/')

    
def GetPlayers(request):
    players = Player.objects.all()
    message = 'No players in list' if len(players) == 0 else 'Has players'

    return HttpResponse(message)
    