from django.urls import path, include

from .api_views import (
    CategoryAPIView,
    BathAPIView,
    BathDetailAPIView
)


urlpatterns = [
    path('categories/', CategoryAPIView.as_view(), name='categories'),
    path('categories/<str:id>/', CategoryAPIView.as_view(), name='categories'),
    path('baths/', BathAPIView.as_view(), name='baths'),
    path('baths/<str:id>/', BathDetailAPIView.as_view(), name='bath_detail'),
]
