from store.models import Customer
from django.shortcuts import redirect, render
from django.views import View
from store.models.product import Product
from store.models.orders import Orders


# Create your views here.
class Checkout(View):
    def get(self,request):
        return redirect('/')

    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer_id')
        cart = request.session.get('cart')
        products = Product.get_product_by_id(list(cart.keys()))
        for product in products:
            order = Orders(customer=Customer(id=customer),
                           product=product,
                           price=product.price,
                           address=address, mobile=phone,
                           quantity=cart.get(str(product.id))
                           )
            order.save()
            request.session['cart']={}
        return redirect('cart')
