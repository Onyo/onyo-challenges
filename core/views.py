from django.shortcuts import render_to_response


def index(request):
    from django.conf import settings

    context = {
        'installed_apps': []
    }

    if 'api.v0.ana' in settings.INSTALLED_APPS:
        context['installed_apps'].append('api.v0.ana')

    if 'api.v0.bob' in settings.INSTALLED_APPS:
        context['installed_apps'].append('api.v0.bob')

    return render_to_response('index.html', context)
