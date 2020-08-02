from django import forms

from .models import Event

class NewTargetForm(forms.Form):
    """Form representing all event without target"""
    event = forms.ModelChoiceField(queryset=None)

    # def __init__(self, athlete_id, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['event'].queryset = Event.objects.exclude(targetresult__athlete__id=athlete_id).distinct()
    #     