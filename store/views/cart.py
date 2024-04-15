from store.models import Customer
from django.shortcuts import redirect, render
from django.views import View
from store.models.product import Product
from django.utils.decorators import method_decorator
from store.auth.middleware import login_required
# Create your views here.


class Cart(View):
    @method_decorator(login_required)
    def get(self, request):
        ids=request.session.get('cart').keys()
        products=Product.get_product_by_id(ids)
        return render(request, 'cart.html',{'products':products})

    def post(self,request):
        return render(request,'cart.html')
