from django.forms import TextInput
from .models import City
from django.forms.widgets import SelectDateWidget
from django import forms


class CityForm(forms.ModelForm):

    class Meta:
        model = City

        fields = ['name']
        widgets = {
           'name': TextInput(attrs={'class': 'input', 'placeholder': 'City Name', }),
        }


class SearchForm(forms.ModelForm):

    date_from = forms.DateField(widget=SelectDateWidget(years=range(2000, 2025), months={
        1: ('1'), 2: ('2'), 3: ('3'), 4: ('4'),
        5: ('5'), 6: ('6'), 7: ('7'), 8: ('8'),
        9: ('9'), 10: ('10'), 11: ('11'), 12: ('12')
    }), required=False)
    date_to = forms.DateField(widget=SelectDateWidget(years=range(2000, 2025), months={
        1: ('1'), 2: ('2'), 3: ('3'), 4: ('4'),
        5: ('5'), 6: ('6'), 7: ('7'), 8: ('8'),
        9: ('9'), 10: ('10'), 11: ('11'), 12: ('12')
    }), required=False)

    name = forms.CharField(required=False)

    class Meta:
        model = City

        fields = ['name', 'date_from', 'date_to']