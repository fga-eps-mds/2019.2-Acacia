# Django
from django.urls import path, include

# Viewsets
from .viewsets import UserRegistrationAPIView, GetUserPreferedLanguage, SetUserPreferedLanguage, TestAccessToken

# Simple JWT
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'users'

urlpatterns = [
    path('signup/', UserRegistrationAPIView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('set-prefered-language/', SetUserPreferedLanguage.as_view(), name='set_prefered_language'),
    path('get-prefered-language/', GetUserPreferedLanguage.as_view(), name='get_prefered_language'),
    path('test-access-token/', TestAccessToken.as_view(), name='test-access-token')
]