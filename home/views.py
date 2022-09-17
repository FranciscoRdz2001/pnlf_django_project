from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def Index(request):
    context = {}
    return render(request, 'base.html', context)