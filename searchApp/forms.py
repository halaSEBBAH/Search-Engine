from django.forms import ModelForm,TextInput

from .models import Candidate


class CandidateForm(ModelForm):
    class Meta:
        model = Candidate
        fields = ['search']
        widgets = {'search': TextInput(attrs={'class': 'input', 'placeholder': 'enter skills here'})}
        
