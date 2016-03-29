from django.conf.urls import url
from .views import Locations, LocationDetail

urlpatterns = [
    url(r'^locations$', Locations.as_view(), name='locations'),
    url(r'^locations/(?P<postcode>[0-9]+)$', LocationDetail.as_view(), name='location-detail'),
]