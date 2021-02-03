from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter

from .serializers import CategorySerializer, BathSerializer
from ..models import Category, Bath


class CategoryListAPIView(ListAPIView):
    """
    Представление апи категорий товаров
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class BathAPIView(ListAPIView):
    """
    Представление апи категорий товаров
    """
    serializer_class = BathSerializer
    queryset = Bath.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['price', 'slug']
    