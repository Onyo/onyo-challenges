from django.conf.urls import url, include
from rest_framework import routers
from zipcode import views

router = routers.DefaultRouter()

router.register(r'zipcode', views.ZipViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
