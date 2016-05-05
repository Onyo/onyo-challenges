from django.conf.urls import include, url

urlpatterns = [
    url(r'^answers/docs/', include('rest_framework_swagger.urls')),
]
