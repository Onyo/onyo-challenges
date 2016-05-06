from django.conf.urls import include, url

from .views import Addresses, AddressDetail

urlpatterns = [
    url(r'^addresses/$', Addresses.as_view(), name='addresses'),
    url(r'^addresses/(?P<postcode>[0-9]+)/$', AddressDetail.as_view(), name='address-detail'),
    url(r'^addresses/docs/', include('rest_framework_swagger.urls')),
]