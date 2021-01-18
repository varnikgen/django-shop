from django import template
from django.utils.safestring import mark_safe

from mainapp.models import Mixer


register = template.Library()

TABLE_HEAD = """
            <table class="table">
                <tbody>
"""
TABLE_CONTENT = """
                    <tr>
                        <td>{name}</td>
                        <td>{value}</td>
                    </tr>
"""
TABLE_TAIL = """
                </tbody>
            </table>
"""
PRODUCT_SPEC = {
    'bath':{
        'Материал': 'material',
        'Длинна': 'length',
        'Ширина': 'width',
    },
    'mixer':{
        'Тип смесителя': 'mixer_type',
        'Тип управления': 'control_type',
        'Цвет': 'color',
        'Материал': 'material',
        'Монтаж': 'mounting',
        'Наличие душа': 'shower',
        'Тип душа': 'type_shower',
    },
}


def get_product_spec(product, model_name):
    table_content = ''
    for name, value in PRODUCT_SPEC[model_name].items():
        table_content += TABLE_CONTENT.format(name=name, value=getattr(product, value))
    return table_content


@register.filter
def product_spec(product): #(product, arg):
    # print(arg, 'arg_value') # Пример передачи дополнительного аргумента
    model_name = product.__class__._meta.model_name
    if isinstance(product, Mixer):
        if not product.shower:
            PRODUCT_SPEC['mixer'].pop('Тип душа')
        else:
            PRODUCT_SPEC['mixer']['Тип душа'] = 'type_shower'
    return mark_safe(TABLE_HEAD + get_product_spec(product, model_name) + TABLE_TAIL)
