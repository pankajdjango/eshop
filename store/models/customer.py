from django.db import models
from django.http import request


class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    contact = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=500)

    def __str__(self):
        return self.first_name
    @staticmethod
    def get_customer_By_Email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

    def register(self):
        return self.save()
