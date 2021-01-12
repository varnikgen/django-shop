from PIL import Image

from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models


User = get_user_model()


class MinResolutionErrorException(Exception):
    pass


class MaxResolutionErrorException(Exception):
    pass


class LatestProductsManager:
    """
    Класс получает список последних продуктов товаров
    """
    @staticmethod
    def get_products_for_main_page(*args, **kwargs):
        """
        метод получает объекты класса товара указанного в аргументах метода
        """
        with_respect_to = kwargs.get('with_respect_to')
        products = []
        ct_models = ContentType.objects.filter(model__in = args)
        for ct_model in ct_models:
            model_products = ct_model.model_class()._base_manager.all().order_by('-id')[:5]
            products.extend(model_products)
        if with_respect_to:
            ct_model = ContentType.objects.filter(model=with_respect_to)
            if ct_model.exists():
                if with_respect_to in args:
                    return sorted(
                        products, key=lambda x: x.__class__._meta.model_name.startswith(with_respect_to), reverse=True
                    )
        return products


class LatestProducts:
    """
    Выборка товара для главной страницы
    """
    objects = LatestProductsManager()


class Category(models.Model):
    """
    Модель категории тваров
    """
    name = models.CharField(max_length=255, verbose_name='Имя категории')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Модель товара
    """

    MIN_RESOLUTION = (300, 300)
    MAX_RESOLUTION = (800, 800)
    MAX_IMAGE_SIZE = 3145728

    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Наименование')
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание', null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """ Метод сохранения модели в базе с учётом ограничений изображени """
        image = self.image
        img = Image.open(image)
        min_height, min_width = self.MIN_RESOLUTION
        max_height, max_width = self.MAX_RESOLUTION
        if min_width > img.width or min_height > img.height:
            raise MinResolutionErrorException('Разрешение изображения не соответствуе минимально разрешённому: 300х300')
        if img.height > max_height or img.width > max_width:
            print(max_height, max_width)
            raise MaxResolutionErrorException('Разрешение изображения не соответствуе максимально разрешённому: 800х800')
        return image

    class Meta:
        abstract = True


class CartProduct(models.Model):
    """
    Модель Товары в корзине
    """
    user = models.ForeignKey('Customer', verbose_name='Покупатель', on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', verbose_name='Корзина', on_delete=models.CASCADE, related_name='related_products')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    qty = models.PositiveIntegerField(default=1)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая стоимость')

    def __str__(self):
        return "Продукт: {} (для корзины)".format(self.product.title)


class Cart(models.Model):
    """
    Модель Корзины
    """
    owner = models.ForeignKey('Customer', verbose_name='Владелец', on_delete=models.CASCADE)
    products = models.ManyToManyField(CartProduct, blank=True, related_name='related_cart')
    total_products = models.PositiveIntegerField(default=0)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая стоимость')

    def __str__(self):
        return str(self.id)


class Customer(models.Model):
    """
    Модель покупателя
    """
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    address = models.CharField(max_length=255, verbose_name='Адрес')

    def __str__(self):
        return "Покупатель: {} {}".format(self.user.first_name, self.user.last_name)





# Типы продуктов
class Bath(Product):
    """
    Модель класса ванн
    """
    material = models.CharField(max_length=50, verbose_name='Материал')
    length = models.PositiveIntegerField(verbose_name='Длинна')
    width = models.PositiveIntegerField(verbose_name='Ширина')
    
    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)


class Mixer(Product):
    """
    Модель класса смесителей
    """
    mixer_type = models.CharField(max_length=50, verbose_name='Тип смесителя')
    control_type = models.CharField(max_length=50, verbose_name='Тип управления')
    color = models.CharField(max_length=50, verbose_name='Цвет')
    material = models.CharField(max_length=50, verbose_name='Материал')
    mounting = models.CharField(max_length=50, verbose_name='Монтаж')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

