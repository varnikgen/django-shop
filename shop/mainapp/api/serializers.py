from rest_framework import serializers

from ..models import Category


class CategorySerializer(serializers.ModelSerializer):
    """
    Сериализатор апи для категорий товаров
    """
    name = serializers.CharField(required=True)
    slug = serializers.SlugField()

    class Meta:
        model = Category
        fields = [
            'id', 'name', 'slug',
        ]
