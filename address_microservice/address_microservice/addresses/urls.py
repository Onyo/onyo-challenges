from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^api/v1/addresses/$',
    views.get_post_address,
    name='get_post_address'),
    url(r'^api/v1/addresses/(?P<id>\d+)$',
    views.get_delete_patch_address,
    name='get_delete_patch_address')
]