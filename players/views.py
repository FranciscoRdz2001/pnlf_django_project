from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Player
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


            p, created = Player.objects.get_or_create(
                name= name,
                age = age,
                number = number,
                nationality = nationality
            )
            p.save()
        return redirect('/')

    form = CreatePlayerForm()
    context = {
        'form': form
    }
    return render(request, 'player/add_player.html', context)
    
def UpdatePlayer(request, pk):

    p = Player.objects.get(pk=pk)

    if request.method == 'POST':
        player = CreatePlayerForm(request.POST)
        print(player.is_valid())
        if player.is_valid():
            p.name = player.cleaned_data.get('name')
            p.age = player.cleaned_data.get('age')
            p.number = player.cleaned_data.get('number')
            p.nationality = player.cleaned_data.get('nationality')
            p.save()
        return redirect('/')

    form = CreatePlayerForm(instance=p)
    context = {
        'action': 'EDIT',
        'form': form
    }
    return render(request, 'player/add_player.html', context)
    
def DeletePlayer(request, pk):
    player = Player.objects.get(pk=pk)
    print(f'Delete method {player.id} ')
    player.delete()
    return redirect('/')

    
def GetPlayers(request):
    players = Player.objects.all()
    message = 'No players in list' if len(players) == 0 else 'Has players'

    return HttpResponse(message)
    