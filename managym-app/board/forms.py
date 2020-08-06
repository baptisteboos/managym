from django import forms

from .models import Event, Information

class NewTargetForm(forms.Form):
    """Form representing all event without target"""
    event = forms.ModelChoiceField(queryset=None)


class SaveInformationForm(forms.Form):
    """
    Form representing a new/edit information
    """
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder': 'What is the injury?',
            	   'class': 'form-control'}
        	),
        max_length=1000,
        help_text='The max length of the text is 1000.'
    )
    information_id = forms.CharField(
        widget=forms.TextInput(
            attrs={'type': 'hidden',
                   'id': 'id_information'}
            )
        )
