from django.http import HttpResponse
from django.shortcuts import render, redirect

from stadiums.forms import CreateStadiumForm

from .models import Stadium

# Create your views here.
def CreateStadium(request):

    print(f'Create player endpoint by request method = {request.method} ')

    if request.method == 'POST':
        stadium = CreateStadiumForm(request.POST)
        if stadium.is_valid():
            name = stadium.cleaned_data.get('name')
            address = stadium.cleaned_data.get('address')
            phone = stadium.cleaned_data.get('phone')
            capacity = stadium.cleaned_data.get('capacity')


            p, created = Stadium.objects.get_or_create(
                name= name,
                address = address,
                phone = phone,
                capacity = capacity
            )
            p.save()
        return redirect('/')

    form = CreateStadiumForm()

    context = {
        'action': 'create',
        'form': form
    }
    return render(request, 'stadiums/add_stadium.html', context)


def UpdateStadium(request, pk):
    s = Stadium.objects.get(pk=pk)

    if request.method == 'POST':
        stadium = CreateStadiumForm(request.POST)
        print(stadium.is_valid())
        if stadium.is_valid():
            s.name = stadium.cleaned_data.get('name')
            s.address = stadium.cleaned_data.get('address')
            s.phone = stadium.cleaned_data.get('phone')
            s.capacity = stadium.cleaned_data.get('capacity')
            s.save()
        return redirect('/')

    form = CreateStadiumForm(instance=s)
    context = {
        'action': 'edit',
        'form': form
    }
    return render(request, 'stadiums/add_stadium.html', context)
    return

def DeleteStadium(request, pk):
    stadium = Stadium.objects.get(pk=pk)
    stadium.delete()
    return redirect('/')

def GetStadiums(request):
    players = Stadium.objects.all()
    
    return