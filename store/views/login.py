from store.models import Customer
from django.shortcuts import redirect, render
from django.contrib.auth.hashers import check_password
from django.views import View
from django.utils.decorators import method_decorator
from store.auth.middleware import already_login
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


class Login(View):
    @method_decorator(already_login)
    @method_decorator(csrf_exempt)

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        error_message = None
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_By_Email(email)
        if customer:
            match_Password = check_password(password, customer.password)
            if match_Password:
                request.session['customer_id'] = customer.id
                request.session['email'] = customer.email
                request.session['user'] = customer.first_name
                return redirect('/')
            else:
                error_message = 'Email or Password Invailed !'
        else:
            error_message = 'Email or Password Invailed !'
        return render(request, 'login.html', {'error': error_message})


def logout(request):
    request.session.clear()
    return redirect('login')
