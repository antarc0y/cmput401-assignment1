"""
WSGI config for TV project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os, sys
# add the hellodjango project path into the sys.path
sys.path.append('<home/ubuntu/cmput401-assignment1/TV>/TV')

# add the virtualenv site-packages path to the sys.path
#sys.path.append('<PATH_TO_VIRTUALENV>/Lib/site-packages')

# poiting to the project settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TV.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


