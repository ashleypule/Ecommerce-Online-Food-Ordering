from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received,invalid_ipn_received

from .models import Order
from django.dispatch import receiver

@receiver(valid_ipn_received)
def valid_ipn_signal(sender, **kwargs):
    ipn = sender
    if ipn.payment_status == ST_PP_COMPLETED:

        Order.objects.create()



@receiver(valid_ipn_received)
def invalid_ipn_signal(sender, **kwargs):
    ipn = sender
    if ipn.payment_status == ST_PP_COMPLETED:

        Order.objects.create()
