from acacia.helpers import list_all_endpoints
from django.urls import path
from .viewsets import (
    UserRegistrationAPIView,
    CreateAccessToken,
    RefreshAccessToken,
    RetrieveUpdatePreferedLanguageAPIView,
    test_access_token
)
app_name = 'users'


urlpatterns = [
    path(
        'signup/',
        UserRegistrationAPIView.as_view(),
        name='register'
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
]


urlpatterns = list_all_endpoints(
    urlpatterns,
    app_name=app_name
)
