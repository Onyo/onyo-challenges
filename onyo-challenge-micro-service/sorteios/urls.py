from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from sorteios import views

urlpatterns = [
    path('sorteios/', views.sorteios_list),
    path('user/<int:ownerpk>/sorteios/', views.sorteios_user_list),
    path('user/<int:ownerpk>/sorteios/<int:pk>/', views.sorteio_view),
    path('sorteios/<int:pk>/resultado/', views.resultado_view),
]

urlpatterns = format_suffix_patterns(urlpatterns)
