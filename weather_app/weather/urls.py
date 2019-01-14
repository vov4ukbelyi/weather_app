from django.conf.urls import url
from . import views
from .views import UpdateView
from dal import autocomplete
from .models import City

app_name = 'weather'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^name-autocomplete/$', UpdateView.as_view(model=City), name='name-autocomplete'),
    url(r'^stored_data/$', views.stored_data, name='stored_data'),
]



class LinkedDataView(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = super(LinkedDataView, self).get_queryset()
        owner = self.forwarded.get('owner', None)

        if owner:
            qs = qs.filter(owner_id=owner)

        return qs
