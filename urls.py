from django.conf.urls import url, include

urlpatterns = [
    url(r'', include('postman.urls')),
    url(r'', include('secretary.urls')),
]