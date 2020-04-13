from django.forms import ModelForm,TextInput

from .models import City

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['search']
        widgets = {'search': TextInput(attrs={'class': 'input', 'placeholder': 'enter skills here'})}