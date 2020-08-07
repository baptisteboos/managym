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
            attrs={'placeholder': 'Write your text, you\'re limited to 1000 characters',
            	   'class': 'form-control'}
        	),
        max_length=1000,
    )
    information_id = forms.CharField(
        widget=forms.TextInput(
            attrs={'type': 'hidden',
                   'id': 'id_information'}
            )
        )
    information_type = forms.CharField(
        widget=forms.TextInput(
            attrs={'type': 'hidden',
                    'id': 'type_information'}
            )
        )
