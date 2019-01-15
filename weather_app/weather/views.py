import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm
from django.views import generic
from django.urls import reverse_lazy
from django_tables2 import RequestConfig
from .tables import CityTable


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
        city.save()
    elif city.data['name'] == 'None':
        pass
    else:
        city.name = city.data['name']
        city.save()

    context = {'form': form, 'city': city}
    return render(request, 'weather/search.html', context)


class UpdateView(generic.UpdateView):
    model = City
    form_class = CityForm
    template_name = 'weather/search.html'
    success_url = reverse_lazy('weather/search.html')

    def get_object(self):
        return City.objects.first()


def stored_data(request):
    table = CityTable(City.objects.all())
    if request.method == 'POST':
        form_city_filter = CityForm(request.POST)
        if form_city_filter.is_valid():
            form_city_filter.save(commit=False)
    cname = request.POST.get('name')
    form_city_filter = CityForm()
    if cname is not None:
        table = CityTable(City.objects.raw('SELECT * FROM weather_city WHERE name = %s', [cname]))
    else:
        pass

    RequestConfig(request, paginate={'per_page': 5}).configure(table)
    context = {'table': table, 'form_city_filter': form_city_filter}
    return render(request, 'weather/base.html', context)


