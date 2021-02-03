from django.urls import path, include

from .api_views import CategoryListAPIView, BathAPIView


urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='categories'),
    path('baths/', BathAPIView.as_view(), name='baths'),
]
