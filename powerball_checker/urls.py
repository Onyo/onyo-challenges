from powerball_checker import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.ListPrizesView().as_view()),

    url(r'^check/', views.VerifyTicketView().as_view()),

    url(r'^create/', views.CreateTicketView().as_view()),
]
