from collections import OrderedDict

from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination

from .serializers import CategorySerializer, BathSerializer
from ..models import Category, Bath


class CategoryPagination(PageNumberPagination):
    """
    Класс пагинации по категориям
    """
    page_size = 2
    page_query_param = 'page_size'
    max_page_size = 10

    # =====================================================================
    # Изменение представления при добавлении пагинации хз зачем оно кому-то
    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('objects_count', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('items', data)
        ]))
    # =====================================================================


class CategoryAPIView(ListCreateAPIView, RetrieveUpdateAPIView):
    """
    Представление апи категорий товаров
    """
    serializer_class = CategorySerializer
    pagination_class = CategoryPagination
    queryset = Category.objects.all()
    
    lookup_field = 'id'


class BathAPIView(ListAPIView):
    """
    Представление апи категорий товаров
    """
    serializer_class = BathSerializer
    queryset = Bath.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['price', 'slug']


class BathDetailAPIView(RetrieveAPIView):
    """
    Представление апи для отображения конкретного товара
    """
    serializer_class = BathSerializer
    queryset = Bath.objects.all()
    lookup_field = 'id'
