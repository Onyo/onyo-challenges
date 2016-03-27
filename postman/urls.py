from django.conf.urls import url
from .views import Locations 

urlpatterns = [
    url(r'^locations$', Locations.as_view(), name='locations'),
]