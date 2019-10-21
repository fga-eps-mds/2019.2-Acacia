# Django
from django.urls import path, include

# Viewsets
from .viewsets import (
    HarvestCreateAPIView
)

app_name = 'harvest'

urlpatterns = [
    path('', HarvestCreateAPIView.as_view(), name='harvestcreate'),
   # path(':id/', HarvestRegistrationAPIView.as_view(), name='harvestcrud'),
]