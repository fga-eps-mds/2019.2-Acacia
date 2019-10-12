from django.urls import path, include
from .viewsets import PropertyListCreateAPIView, PropertyDetailAPIView

app_name = 'property'

urlpatterns = [
    path(
        '', 
        PropertyListCreateAPIView.as_view(), 
        name='list'
        ),

    path(
        '<int:pk>/', 
        PropertyDetailAPIView.as_view(), 
        name='detail'
    ),
]