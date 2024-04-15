from django.db import models
from  .product import Product
from .customer import Customer
import datetime
class Orders(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    price=models.IntegerField()
    address=models.CharField(max_length=50 ,default='',blank=True)
    mobile=models.CharField(max_length=10,default='',blank=True)
    date=models.DateField(default=datetime.datetime.today)
    status=models.BooleanField(default=False)

    def __str__(self):
        # return self.customer.first_name
        return self.product.name

    @staticmethod
    def get_orders_by_customer_id(customer_id):
        return Orders.objects.filter(customer = customer_id).order_by('date')
