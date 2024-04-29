
from django.urls import path
from . import views

urlpatterns = [
   
   
    path('payment_success', views.payment_success, name='payment_success'),

    path('payment_pay', views.payment_pay, name='payment_pay'),
    
    path('paypal-return', views.paypal_return, name='paypal-return'),
    path('pay-cancel', views.paypal_cancel, name='paypal-cancel'),

    
]
