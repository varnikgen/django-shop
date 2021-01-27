from django.views.generic import View
from django.views.generic.detail import SingleObjectMixin

from .models import Category, Cart, Customer, Bath, Mixer


class CategoryDetailMixin(SingleObjectMixin):
    """
    Миксин для CategoryDetail выводит информацию о категориях
    """
    CATEGORY_SLUG2PRODUCT_MODEL = {
        'baths': Bath,
        'mixers': Mixer,
    }
    def get_context_data(self, **kwargs):
        if isinstance(self.get_object(), Category):
            model = self.CATEGORY_SLUG2PRODUCT_MODEL[self.get_object().slug]
            context = super().get_context_data(**kwargs)
            context['categories'] = Category.objects.get_categories_for_left_sidebar()
            context['category_products'] = model.objects.all()
            return context
        else:
            context = super().get_context_data(**kwargs)
            context['categories'] = Category.objects.get_categories_for_left_sidebar()
            return context


class CartMixin(View):
    """
    Миксин для CartView выводит информацию о категориях
    """
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            customer = Customer.objects.filter(user=request.user).first()
            if not customer:
                customer = Customer.objects.create(user=request.user)
            cart = Cart.objects.filter(owner=customer, in_order=False).first()
            if not cart:
                cart = Cart.objects.create(owner=customer)
        else:
            cart = Cart.objects.filter(for_anonimus_user=True).first()
            if not cart:
                cart = Cart.objects.create(for_anonimus_user=True)
        self.cart = cart
        return super().dispatch(request, *args, **kwargs)
