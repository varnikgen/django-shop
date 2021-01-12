from PIL import Image

from django.forms import ModelChoiceField, ModelForm, ValidationError
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class BathAdminForm(ModelForm):
    """
    Класс формы раздела ванн в админке
    MIN_RESOLUTION - минимальное разрешение для изображений товара
    """
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].help_text = mark_safe(
            """<span style="color:red; font-size:14px;">Изображение разрешением больше {}x{} будет сжато</span>
            """.format(*Product.MAX_RESOLUTION)
        )

    # def clean_image(self):
    #     image = self.cleaned_data['image']
    #     img = Image.open(image)
    #     min_height, min_width = Product.MIN_RESOLUTION
    #     max_height, max_width = Product.MAX_RESOLUTION
    #     if image.size > Product.MAX_IMAGE_SIZE:
    #         raise ValidationError('Размер изображения превышает 3МБ')
    #     if min_width > img.width or min_height > img.height:
    #         raise ValidationError('Разрешение изображения не соответствуе минимально разрешённому: 300х300')
    #     if img.height > max_height or img.width > max_width:
    #         print(max_height, max_width)
    #         raise ValidationError('Разрешение изображения не соответствуе максимально разрешённому: 800х800')
    #     return image



class BathAdmin(admin.ModelAdmin):
    """
    Класс представляющий ванны в админке
    """

    form = BathAdminForm
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """
        Метод оставляет возможность в админке в ваннах выбирать только категорию Ванны
        """
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='baths'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class MixerAdmin(admin.ModelAdmin):
    """
    Класс представляющий смесители в админке
    """
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """
        Метод оставляет возможность в админке в ваннах выбирать только категорию Смесителей
        """
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='mixers'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category)
admin.site.register(Bath, BathAdmin)
admin.site.register(Mixer, MixerAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)