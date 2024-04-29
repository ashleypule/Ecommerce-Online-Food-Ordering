from django.db import models
from django.contrib.auth.models import User
from core.models import Product

# Create your models here.

class ShippingAddress(models.Model):

    user= models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    shipping_full_name = models.CharField(max_length=255)
    shipping_email = models.CharField(max_length=255)
    shipping_address = models.CharField(max_length=255)
    shipping_city = models.CharField(max_length=255)
    shipping_zipcode = models.CharField(max_length=255, null=True, blank=True)
    shipping_country = models.CharField(max_length=255)


    class Meta:

        verbose_name_plural = "Shipping Address"

    def __str__(self):
        return f'shipping Address - {str(self.id)}'


# create order Model
    
class Order(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    full_name = models.CharField(max_length=250)
    email= models.EmailField(max_length=250)
    address = models.TextField(max_length=17000)
    amount_paid = models.DecimalField(max_digits=10 , decimal_places= 2)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'order - {str(self.id)}'
    



     

