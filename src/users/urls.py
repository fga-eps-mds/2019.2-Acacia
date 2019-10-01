# Django
from django.urls import path, include

# Viewsets
from .viewsets import UserRegistrationAPIView

# Simple JWT
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'users'

urlpatterns = [
<<<<<<< HEAD
    path('signup/', UserRegistrationAPIView.as_view(), name='signup'),
=======
    path('signup/', UserRegistrationAPIView.as_view(), name='register'),
>>>>>>> f31e1452b216abcc05a194a3985b768a7eff4b1e
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]