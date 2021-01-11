from django.forms import ModelChoiceField
from django.contrib import admin

from .models import *


class BathAdmin(admin.ModelAdmin):
    """
    Класс представляющий ванны в админке
    """
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