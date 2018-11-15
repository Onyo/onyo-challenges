from django.urls import include, path
from rest_framework.routers import DefaultRouter

from cep import views

router = DefaultRouter()
router.register(r'staties', views.StateViewSet)
router.register(r'cities', views.CityViewSet)

urlpatterns = [path("", include(router.urls))]
