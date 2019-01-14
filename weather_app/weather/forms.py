from django.forms import TextInput
from .models import City
import django_filters
from dal import autocomplete
from django import forms


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {
            'name' : TextInput(attrs={'class': 'input', 'placeholder': 'City Name'}),
            #'name' : autocomplete.(url='weather:name-autocomplete')
        }


class CityFilter(django_filters.FilterSet):
    class Meta:
        model = City
        fields = ['name', 'created']

