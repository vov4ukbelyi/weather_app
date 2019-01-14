import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm, CityFilter
from django.views import generic
from django.urls import reverse_lazy
from django_tables2 import RequestConfig
from .tables import CityTable
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=831404ac4314d3d14d7afbe6b6265d92'

    if request.method == 'POST':
        form = CityForm(request.POST)
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


    context = {'form': form,'city': city}
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
    RequestConfig(request, paginate={'per_page': 5}).configure(table)

    filter = CityFilter(request.GET, queryset=City.objects.all())

    class FilteredCityListView(SingleTableMixin, FilterView):
        table_class = CityTable
        model = City
        template_name = 'weather/base.html'
        filterset_class = CityFilter
    context = {'table': table, 'filter': filter}
    return render(request, 'weather/base.html', context)




class FilteredCityListView(SingleTableMixin, FilterView):
    table_class = CityTable
    model = City
    template_name = 'weather/base.html'
    filterset_class = CityFilter

