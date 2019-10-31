from django.urls import path

# Viewsets
from .viewsets import (
    UserRegistrationAPIView,
    RetrieveUpdatePreferedLanguageAPIView,
    test_access_token,
    CreateAccessToken,
    RefreshAccessToken,
)


app_name = 'users'

urlpatterns = [
    path(
        'signup/',
        UserRegistrationAPIView.as_view(),
        name='register'
    ),

    path(
        'token/',
        CreateAccessToken.as_view(),
        name='token_obtain_pair'
    ),

    path(
        'token/refresh/',
        RefreshAccessToken.as_view(),
        name='token_refresh'
    ),

    path(
        'prefered-language/',
        RetrieveUpdatePreferedLanguageAPIView.as_view(),
        name='set_prefered_language'
    ),

    path(
        'token/test-access-token/',
        test_access_token,
        name='test_access_token'
    ),
]
