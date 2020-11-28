from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from currency import consumer

websocket_urlPattern=[
	path("ws/faitsData", consumer.FaitsConsumer),
]

application = ProtocolTypeRouter({
	'websocket': AuthMiddlewareStack(URLRouter(websocket_urlPattern))
})