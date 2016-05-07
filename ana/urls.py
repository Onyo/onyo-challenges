from django.conf.urls import include, url

from .views import Records, RecordDetail

urlpatterns = [
    url(r'^records/$', Records.as_view(), name='records'),
    url(r'^records/(?P<pk>[0-9]+)/$', RecordDetail.as_view(), name='record-detail'),
    url(r'^records/docs/', include('rest_framework_swagger.urls')),
]
