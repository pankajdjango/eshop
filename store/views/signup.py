from store.models import Customer
from django.shortcuts import redirect, render
from django.contrib.auth.hashers import make_password
from django.views import View
from django.utils.decorators import method_decorator
from store.auth.middleware import already_login

# Create your views here.

class Signup(View):
    @method_decorator(already_login)
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        return self.registerUser(request)

    def registerUser(self,request):
        first_name = request.POST.get('fname',None)
        last_name = request.POST.get('lname',None)
        contact = request.POST.get('contact',None)
        email = request.POST.get('email',None)
        password = request.POST.get('password',None)
        confirm_password = request.POST.get('re-password',None)

        # value after error fill old data
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'contact': contact,
            'email': email,
            'password': '',
        }
        # Form validate
        error_message = None
        if len(first_name) < 4:
            error_message = "First name must be 4 Char long or more !"
        elif len(last_name) < 4:
            error_message = "Last name must be 4 Char long or more !"
        elif len(contact) < 10 or len(contact) > 10:
            error_message = "Contact must be 10 digit !"
        elif len(password) < 4:
            error_message = "Password too short !"
        elif password != confirm_password:
            error_message = "Password dit not match !"
        # Check for email match on database
        elif Customer.objects.filter(email=email).exists():
            error_message = 'Email Already Registered'
        elif Customer.objects.filter(contact=contact).exists():
            error_message = 'Contact Already Registered'
        # end validations
        if not error_message:
            customer = Customer(first_name=first_name, last_name=last_name, contact=contact, email=email, password=password)
            customer.password = make_password(password)
            customer.register()
            return redirect('login')
        else:
            data = {
                'error': error_message,
                'value': value
            }
            return render(request, 'signup.html', data)
