from django.views.generic import View

from .models import Category, Cart, Customer


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
