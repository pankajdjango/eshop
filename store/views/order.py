from store.models import Customer
from django.shortcuts import redirect, render
from django.views import View
from store.models.product import Product
from store.models.orders import Orders
from django.utils.decorators import method_decorator
from store.auth.middleware import login_required


# Create your views here.

class Order_View(View):
    @method_decorator(login_required)
    def get(self, request):
        customer = request.session.get('customer_id')
        orders = Orders.get_orders_by_customer_id(customer)
        return render(request,'orders.html',{'orders':orders})
