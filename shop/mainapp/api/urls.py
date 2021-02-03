from django.urls import path, include

from .api_views import CategoryListAPIView


urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='categories'),
]
