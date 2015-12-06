

class BootstrapViewTest:

    def setup_view(self, view, request, user=None, *args, **kwargs):
        """Retirado de
        <http://tech.novapost.fr/django-unit-test-your-views-en.html>
        Mimic as_view() returned callable, but returns view instance.
        args and kwargs are the same you would pass to ``reverse()``
        """
        view.request = request
        view.args = args or []
        view.kwargs = kwargs or {}

        if user:
            self._config_user(request, user)

        # TODO: session e messages quando houver necessidade
        return view

    def _config_user(self, request, user):
        from django.contrib.sessions.middleware import SessionMiddleware
        from django.contrib.auth import login

        SessionMiddleware().process_request(request)

        user.backend = None
        request.user = user
        login(request, user)

    def dispatch_view(self, view):
        return view.dispatch(view.request, *view.args, **view.kwargs)
