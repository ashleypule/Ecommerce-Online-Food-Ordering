import uuid

from django.shortcuts import render,redirect
from django.contrib import messages
from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm

from django.conf import settings

# Create your views here.

def payment_success(request):

    
    host = request.get_host()

    paypal_dict = {

        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': '{{ totals }}',
        'item_name': 'product 1',
        'invoice': str(uuid.uuid4()),
        'currency_code': 'USD',
        'notify_url': f'http://{host}{reverse("paypal-ipn")}',
        'return_url': f'http://{host}{reverse("paypal-return")}',
        'cancel_return': f'http://{host}{reverse("paypal-cancel")}',
        



    }

    form = PayPalPaymentsForm(initial = paypal_dict)
    context = {'form':form}

    #return render(request, 'payment_pay.html', {'form':form})
    return render(request, "payment/payment_success.html", context)

def payment_pay(request):
    pass
def paypal_return(request):

    messages.success(request,'You\'ve successfully made a payment!')

    return redirect('payment_success')

def paypal_cancel(request):

    messages.error(request,'Your order have been cancelled!')

    return redirect('payment_success')
