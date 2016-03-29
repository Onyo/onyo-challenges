from django.conf.urls import url
from .views import Locations, LocationDetail, index

urlpatterns = [
	url(r'^locations$', Locations.as_view(), name='locations'),
    url(r'^locations/(?P<postcode>[0-9]+)$', LocationDetail.as_view(), name='location-detail'),
    url(r'^locations/index$', index, name='locations-index'),
]