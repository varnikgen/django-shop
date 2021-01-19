from django.shortcuts import render
from django.views.generic import DetailView

from .models import Bath, Mixer, Category


def test_view(request):
    categories = Category.objects.get_categories_for_left_sidebar()
    return render(request, 'base.html', {'categories': categories})


class ProductDetailView(DetailView):
    """
    Класс для представления всех продуктовых классов из моделей в одном шаблоне
    """
    CT_MODEL_MODEL_CLASS = {
        'bath': Bath,
        'mixer': Mixer,
    }

    def dispatch(self, request, *args, **kwargs):
        self.model = self.CT_MODEL_MODEL_CLASS[kwargs['ct_model']]
        self.queryset = self.model._base_manager.all()
        return super().dispatch(request, *args, **kwargs)

    context_object_name = 'product'
    template_name = 'product_detail.html'
    slug_url_kwarg = 'slug'
