from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^api/v1/employees/$',
    views.get_post_employees,
    name='get_post_employees'),
    url(r'^api/v1/employees/(?P<id>\d+)$',
    views.get_delete_patch_employee,
    name='get_delete_patch_employee')
]