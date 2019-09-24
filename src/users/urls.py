from django.urls import path
from .viewsets import registration_view

app_name = 'users'

urlpatterns = [
    path('register/', registration_view, name='register'),
]