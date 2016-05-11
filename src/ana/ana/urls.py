from django.conf.urls import url, include
from rest_framework import routers
from customer import views

router = routers.DefaultRouter()

router.register(r'customer', views.CustomerViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
