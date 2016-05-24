from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^tickets/$', views.TicketsView.as_view()),
    url(r'^tickets/(?P<pk>[0-9]+)$', views.TicketsDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
