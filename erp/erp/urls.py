from django.urls import include, path
from rest_framework.routers import DefaultRouter

from erp import views

router = DefaultRouter()
router.register(r'employees', views.EmployeeViewSet)

urlpatterns = [path("", include(router.urls))]
