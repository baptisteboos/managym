from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.db.models import Sum, F

from .models import Athlete, Event, TargetResult, Round2
from .forms import NewTargetForm

def index(request):
    return render(request, 'board/index.html', {})

@method_decorator(login_required, name='dispatch')
class BoardListView(ListView):
    # model = Athlete
    context_object_name = 'athletes'
    template_name = 'board/board.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

    def get_queryset(self):
        queryset = Athlete.objects.filter(
            group__trainers__id=self.request.user.pk).order_by('first_name', 'last_name')
        return queryset

@method_decorator(login_required, name='dispatch')
class AthletesListView(ListView):
    # model = Athlete
    context_object_name = 'athletes'
    template_name = 'board/athletes.html'
    paginate_by = 20
    queryset = Athlete.objects.order_by('first_name', 'last_name')


@login_required
def athlete_detail(request, athlete_id):
    athlete = get_object_or_404(Athlete, id=athlete_id)
    events_participated = Event.objects.filter(targetresult__athlete=athlete).distinct().all()
    for event in events_participated:
        event.targets_results = TargetResult.objects.filter(athlete=athlete, event=event).values(\
            'target_sv', 'target_ex', 'result_sv', 'result_ex', 'apparatus__id', 'apparatus__name')
    new_target_form = NewTargetForm()
    new_target_form.fields['event'].queryset = Event.objects.exclude(
        targetresult__athlete__id=athlete_id).distinct()


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

def athlete_update_target(request, athlete_id):
    if request.is_ajax and request.method == "POST":
        event_id = request.POST.get('event_id', None)
        apparatus_id = request.POST.get('apparatus_id', None)
        target_result = TargetResult.objects.get(athlete__id=athlete_id, event__id=event_id, \
                                                      apparatus__id=apparatus_id)
        target_result.target_sv = request.POST.get('tsv', None)
        target_result.target_ex = request.POST.get('tex', None)
        target_result.result_sv = request.POST.get('rsv', None)
        target_result.result_ex = request.POST.get('rex', None)

    # athlete_event = AthleteEvent.query.filter_by(athlete_id=id, \
    #                                              event_id=event_id).first()
    # athlete_event.target_total = request.form['target']
    # athlete_event.result_total = request.form['result']
    target_result.save()
    data = {
        'success': 'success'
    }
    return JsonResponse(data)

def athlete_graph_get_data(request, athlete_id):
    labels = []
    targets_list = []
    results_list = []
    success = []

    queryset = TargetResult.objects.filter(athlete__id=athlete_id).values(\
        'event__name').annotate(target_total=Round2(Sum('target_sv') + Sum('target_ex'), 2),
                                result_total=Round2(Sum('result_sv') + Sum('result_ex'), 2), 
                                success=Round2(F('result_total') / F('target_total') * 100, 2))
    for entry in queryset:
        labels.append(entry['event__name'])
        targets_list.append(entry['target_total'])
        results_list.append(entry['result_total'])
        success.append(entry['success'])
    
    return JsonResponse(data={
        'labels': labels,
        'targets': targets_list,
        'results': results_list,
        'success': success
    })

