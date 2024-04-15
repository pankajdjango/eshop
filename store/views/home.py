from django.shortcuts import redirect, render
from store.models.product import Product
from store.models.category import Category
from django.views import View
from store.models.customer import Customer


# Create your views here.
class Home(View):
    print("\n\n##################################################\n\n")
    def post(self,request):
        product = request.POST.get('product')
        cart = request.session.get('cart')
        remove = request.POST.get('remove')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1
                else:
                    cart[product] = quantity+1
            else:
                cart[product] = 1
        else:
            cart={}
            cart[product] = 1
        request.session['cart'] = cart
        return redirect('/')

    def get(self,request):
        data,products = {},None
        cart = request.session.get('cart')
        category_id = request.GET.get('category')
        if not cart:
            request.session['cart']={}
        categories = Category.get_all_categories()
        products = Product.get_all_product_by_id(category_id) if category_id else Product.get_all_products()
        data['products'] = products
        data['categories'] = categories
        return render(request, 'index.html', data)
