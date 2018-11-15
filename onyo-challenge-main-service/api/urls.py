from django.urls import include, path
from api import views

urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('sorteios/', views.list_sorteios),
    path('sorteios/<int:pk>/', views.sorteio),
    path('sorteios/<int:pk>/resultado/', views.resultado)
]
