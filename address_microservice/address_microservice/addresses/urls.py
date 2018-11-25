from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^api/v1/address/$',
    views.get_post_address,
    name='get_post_address')
]