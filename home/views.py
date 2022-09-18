from django.shortcuts import render

from players.models import Player
from teams.models import Team
from stadiums.models import Stadium

# Create your views here.
def Index(request):

    teams = Team.objects.all()
    players = Player.objects.all()

    # player = Player()
    # player.age = 21
    # player.name = 'Francisco Rodriguez'
    # player.nationality = 'Mexicano'
    # player.number = 6643525473

    # Player.objects.create()
    # player.save()

    print(len(players))

    for player in players:
        print(player)


    stadiums = Stadium.objects.all()
    context = {
        'teams_list': teams,
        'players_list': players,
        'stadiums_list': stadiums
    }
    return render(request, 'base.html', context)