from django.conf.urls import url, include
from rest_framework import routers
from bob.zipcode import views

router = routers.DefaultRouter()

router.register(r'zipcode', views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
