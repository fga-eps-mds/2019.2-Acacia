from django.urls import path
from .viewsets import UserRegistrationAPIView

app_name = 'users'

urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view(), name='register'),
]