from django.conf.urls import url, include
from .views import Contacts, ContactDetail, index

urlpatterns = [
    url(r'^contacts$', Contacts.as_view(), name='contacts'),
    url(r'^contacts/(?P<pk>[0-9]+)$', ContactDetail.as_view(), name='contact-detail'),
    url(r'^contacts/index$', index, name='contacts-index'),
    url(r'^docs/', include('rest_framework_swagger.urls')),
]