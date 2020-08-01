from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.decorators.http import require_POST 
from django.contrib.auth.decorators import login_required

from .models import Athlete, Event
from .forms import NewTargetForm

@login_required
def index(request):
    athletes = Athlete.objects.all()
    context = {
    	'title': 'Home',
       	'name': 'Baptiste',
       	'athletes': athletes
       }
    return render(request, 'board/index.html', context)


@login_required
def athlete_listing(request):
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

@login_required
def athlete_detail(request, athlete_id):
    athlete = get_object_or_404(Athlete, id=athlete_id)
    events_participated = Event.objects.filter(targetresult__athlete__id=athlete_id).distinct().all()
    new_target_form = NewTargetForm(athlete_id)
   

    context = {
        'title': 'Athlete',
        'athlete': athlete,
        'events_participated': events_participated,
        'form': new_target_form
    }
    return render(request, 'board/athlete.html', context)

@login_required
def athlete_new_target(request, athlete_id):
    if request.method == 'POST':
        athlete = get_object_or_404(Athlete, pk=athlete_id)
        event_id = request.POST.get('event')
        # Male apparatus: 1=floor, 2=pommel horse, 3=rings, 4=vault, 5=parallel bars, 6=high bar
        if athlete.gender == 1:
            [athlete.targetresult_set.create(event_id=event_id, apparatus_id=i, target_sv=0,\
                target_ex=0, result_sv=0, result_ex=0) for i in range(1, 7)]
        # Female apparatus: 1=floor, 4=vault, 7=uneven bars, 8=balance beam
        elif athlete.gender == 2:
            [athlete.targetresult_set.create(event_id=event_id, apparatus_id=i, target_sv=0,\
                target_ex=0, result_sv=0, result_ex=0) for i in [1,4,7,8]] 
    return redirect(reverse('board:athlete_detail', args=[athlete_id]))

