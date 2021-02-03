from rest_framework import serializers

from ..models import Category, Bath, Mixer


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


class BaseProductSerializer:
    """
    Базовый класс продуктов
    """
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects)
    title = serializers.CharField(required=True)
    slug = serializers.SlugField(required=True)
    image = serializers.ImageField(required=True)
    description = serializers.CharField(required=False)
    price = serializers.DecimalField(max_digits=9, decimal_places=2, required=True)


class BathSerializer(BaseProductSerializer, serializers.ModelSerializer):
    """
    Сериализатор апи для модели Ванны
    """
    material = serializers.CharField(required=True)
    length = serializers.IntegerField(required=True)
    width = serializers.IntegerField(required=True)

    class Meta:
        model = Bath
        fields = '__all__'

