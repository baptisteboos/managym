from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import Athlete, Event


def index(request):
    athletes = Athlete.objects.all()
    context = {
    	'title': 'Home',
       	'name': 'Baptiste',
       	'athletes': athletes
       }
    return render(request, 'board/index.html', context)

def listing(request):
    athletes_list = Athlete.objects.order_by('last_name', 'first_name')
    # Slices pages
    paginator = Paginator(athletes_list, 25)
    # Get current page number
    page = request.GET.get('page')
    try:
    	athletes = paginator.page(page)
    except PageNotAnInteger:
    	athletes = paginator.page(1)
    except EmptyPage:
    	# If page is out of range (e.g. 9999), delivers last page of results
        athletes = paginator.page(paginator.num_pages)
    context = {
    	'title': 'Listing',
    	'athletes': athletes
    }
    return render(request, 'board/athletes.html', context)

def athlete_detail(request, athlete_id):
    athlete = get_object_or_404(Athlete, id=athlete_id)
    events_participated = Event.objects.filter(targetresult__athlete__id=athlete_id).distinct().all()

    context = {
        'title': 'Athlete',
        'athlete': athlete,
        'events_participated': events_participated,
    }
    return render(request, 'board/athlete.html', context)
