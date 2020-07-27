from django.shortcuts import render

from .models import Athlete

def index(request):
    athletes = Athlete.objects.all()
    return render(request, 'athletes/index.html', {'title': 'Salut',
                                                   'name': 'Baptiste',
                                                   'athletes': athletes})

def listing(request):
    return render(request, 'athletes/index.html', {} )
