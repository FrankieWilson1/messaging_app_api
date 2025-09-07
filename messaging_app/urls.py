# messaging_app/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from chats.views import UserRegistrationView, UserDocsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', UserDocsView.as_view(), name='api-docs'),
    path(
        'api/v1/register/',
        UserRegistrationView.as_view(),
        name='register'
    ),
    path('api/v1/', include('chats.urls')),
    path(
        'api/v1/token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'api/v1/token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),
    path('api-auth/', include('rest_framework.urls')),
]
