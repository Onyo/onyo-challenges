# -*- coding: utf-8 -*-
from django.contrib import admin
from django.conf import settings
from django.conf.urls import include, url
from django.views.static import serve

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^static/(?P<path>.*)$', serve, {
        'document_root': settings.STATIC_ROOT,
    }),
]

if 'api.v0.ana' in settings.INSTALLED_APPS:
    urlpatterns += [
        url(r'^api/v0/ana/', include('api.v0.ana.urls', namespace='ana')),
    ]

if 'api.v0.bob' in settings.INSTALLED_APPS:
    urlpatterns += [
        url(r'^api/v0/bob/', include('api.v0.bob.urls', namespace='bob')),
    ]
