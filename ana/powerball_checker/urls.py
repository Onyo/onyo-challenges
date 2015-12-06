from powerball_checker import views
from django.conf.urls import url, include

urlpatterns = [
    url(r'^check', views.VerifyTicketView().as_view()),
]
