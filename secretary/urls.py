from django.conf.urls import url
from .views import Contacts, ContactDetail

urlpatterns = [
    url(r'^contacts$', Contacts.as_view(), name='contacts'),
    url(r'^contacts/(?P<pk>[0-9]+)$', ContactDetail.as_view(), name='contact-detail'),
]