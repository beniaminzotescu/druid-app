from django.urls import path
from .views import TestJsonAPIView

urlpatterns = [
    path('test-json/', TestJsonAPIView.as_view(), name='test-json'),
    path('test-json/<str:url>/', TestJsonAPIView.as_view(), name='test-json-detail'),
]

