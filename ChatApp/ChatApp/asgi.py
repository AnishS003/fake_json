# asgi.py

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
import appone.routing  # Import the routing configuration for your app

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ChatApp.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': URLRouter(
        # Include your app's WebSocket URL patterns here
        appone.routing.websocket_urlpatterns
    ),
})
