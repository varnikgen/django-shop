from django.forms import ModelChoiceField, ModelForm
from django.contrib import admin

from .models import *


class MixerAdminForm(ModelForm):
    """
    Рендеринг формы админки с учётом отключения параметров
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if not instance.shower:
            self.fields['type_shower'].widget.attrs.update({
                'readonly': True, 'style':'background: lightgray'
            })
    
    def clean(self):
        if not self.cleaned_data['shower']:
            self.cleaned_data['type_shower'] = None
        return self.cleaned_data



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

    # Для теста отключения раздела в админке
    change_form_template = 'admin.html'
    form = MixerAdminForm
    # =====================================

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