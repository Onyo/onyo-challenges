from django.conf.urls import url
from .views import Contacts

urlpatterns = [
    url(r'^contacts$', Contacts.as_view(), name='contacts'),
]