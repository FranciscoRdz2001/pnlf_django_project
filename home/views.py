from django.shortcuts import render

from players.models import Player
from teams.models import Team
from stadiums.models import Stadium

# Create your views here.
def Index(request):

    teams = Team.objects.all()
    players = Player.objects.all()

    stadiums = Stadium.objects.all()
    context = {
        'teams_list': teams,
        'players_list': players,
        'stadiums_list': stadiums
    }
    return render(request, 'base.html', context)