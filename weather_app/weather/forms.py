from django.forms import TextInput
from .models import City
from django.forms.widgets import SelectDateWidget
from dal import autocomplete
from django import forms


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {
            'name' : TextInput(attrs={'class': 'input', 'placeholder': 'City Name'}),
            #'date' : forms.DateField(widget=SelectDateWidget(empty_label="Nothing"))
            #'name' : autocomplete.(url='weather:name-autocomplete')
        }

