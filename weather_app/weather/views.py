import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm, SearchForm
from django_tables2 import RequestConfig
from .tables import CityTable
import json
from django.http import HttpResponse


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=831404ac4314d3d14d7afbe6b6265d92'

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
    name = request.POST.get('name')
    form = CityForm()

    city = City()
    city.data = requests.get(url.format(name)).json()

    if city.data['cod'] == '404':
        city.name = name
        print(city.name)
    elif city.data['name'] == 'None':
        print(city.data['name'])
        pass
    else:
        city.name = city.data['name']
        city.save()

    context = {'form': form, 'city': city}
    return render(request, 'weather/search.html', context)


def stored_data(request):
    form_city_filter = SearchForm()

    table = CityTable(City.objects.all())

    if request.method == 'POST':
        form_city_filter = SearchForm(request.POST)
        if form_city_filter.is_valid():
            date_from = form_city_filter.cleaned_data.get('date_from')
            date_to = form_city_filter.cleaned_data.get('date_to')
            form_city_filter.save(commit=False)
    cname = request.POST.get('name')

    if cname and date_to == None and date_from == None:
        table = CityTable(City.objects.raw('SELECT * FROM weather_city WHERE name = %s', [cname]))
    elif cname == '' and date_from and date_to:
        table = CityTable(
            City.objects.raw('SELECT * FROM weather_city WHERE created BETWEEN %s AND %s', [date_from, date_to]))
    elif cname and date_from and date_to:
        table = CityTable(City.objects.raw('SELECT * FROM weather_city WHERE name = %s AND created BETWEEN %s AND %s  ',
                                           [cname, date_from, date_to]))
    else:
        pass

    RequestConfig(request, paginate={'per_page': 5}).configure(table)

    context = {'table': table, 'form_city_filter': form_city_filter}
    return render(request, 'weather/base.html', context)


def autocompleteModel(request):
    if request.is_ajax():
        q = request.GET.get('term', '').capitalize()
        search_qs = City.objects.filter(name__startswith=q)
        results = []
        for r in search_qs:
            results.append(r.name)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)