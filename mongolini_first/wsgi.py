"""
WSGI config for mongolini_first project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

<<<<<<< HEAD
from django.core.wsgi import get_wsgi_application #type: ignore
=======
from django.core.wsgi import get_wsgi_application
>>>>>>> 68cdfb849ce52235a489914a0e13f457e181b026

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mongolini_first.settings')

application = get_wsgi_application()
