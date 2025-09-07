# messaging_app/chats/urls.py
from django.urls import path
from rest_framework_nested import routers

from .views import (
    UserViewSet,
    ConversationViewSet,
    MessageViewSet,
    UserProfileView,
    LoginView,
)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'conversations', ConversationViewSet)

conversations_router = routers.NestedSimpleRouter(
    router,
    r'conversations',
    lookup='conversation'
)
conversations_router.register(
    r'messages',
    MessageViewSet,
    basename='conversation-messages'
)

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('users/me/', UserProfileView.as_view(), name='user-profile'),
]
urlpatterns += router.urls
urlpatterns += conversations_router.urls
