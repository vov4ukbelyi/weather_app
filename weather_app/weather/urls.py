from django.conf.urls import url
from . import views

app_name = 'weather'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^stored_data/$', views.stored_data, name='stored_data'),
]

