from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.orders import Orders

# Register your models here.
class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']
    list_filter = ['price','category']
    search_fields = ['name']
    change_list_template = ''


class CustomerAdminShow(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'contact', 'email', 'password']


admin.site.register(Product, AdminProduct)
admin.site.register(Category)
admin.site.register(Customer, CustomerAdminShow)
admin.site.register(Orders)
