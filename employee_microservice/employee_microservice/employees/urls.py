from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^api/v1/employees',
    views.get_all_employees,
    name='get_all_employees')
]