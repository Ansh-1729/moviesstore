"""
Django, being a web framework, needs a web server to operate. And since most web servers 
dont natively speak Python, we need an interface to make that communication happen.

ASGI config for moviesstore project. The asgi.py file contains an entry point for 
ASGI-compatible web servers to serve your project asynchronously.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'moviesstore.settings')

application = get_asgi_application()
