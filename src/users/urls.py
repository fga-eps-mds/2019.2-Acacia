from django.urls import path
from .viewsets import UserRegistrationAPIView

from rest_framework.authtoken.views import obtain_auth_token

app_name = 'users'

urlpatterns = [
    path('signup/', UserRegistrationAPIView.as_view(), name='signup'),
]