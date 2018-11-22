from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^api/v1/employees/$',
    views.get_all_employees,
    name='get_all_employees'),
    url(r'^api/v1/employees/(?P<id>\d+)$',
    views.get_one_employee,
    name='get_one_employee')
]