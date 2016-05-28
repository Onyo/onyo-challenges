from django.conf.urls import include, url

urlpatterns = [
    url(r'^', include('tombola.urls')),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^docs/', include('rest_framework_swagger.urls')),
]
