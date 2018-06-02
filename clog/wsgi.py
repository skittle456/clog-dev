"""
WSGI config for clog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "clog.settings")

application = get_wsgi_application()
if 'runserver' in sys.argv:
    from django.conf import settings
    import inspect
    if settings.DEBUG:
        has_staticfiles = any(
            "django/contrib/staticfiles/management/commands/runserver"
            in x[1]
            for x in inspect.stack())

if has_staticfiles:
    print('runserver with staticfiles detected, skipping whitenoise')
else:
    # Do not use whitenoise with runserver, as it's slow
    from whitenoise.django import DjangoWhiteNoise
    application = DjangoWhiteNoise(application)
