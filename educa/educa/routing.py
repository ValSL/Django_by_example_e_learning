from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing

#  если не будет найдено соответствий то управление автоматически перейдет на стандартные вьюхи
application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(URLRouter(chat.routing.websocket_urlpatterns)),
})
