from django.test import TestCase
from .models import DeliveryReceipt, QuantityOrdered


# Create your tests here.
x = DeliveryReceipt.objects.get(dr_number = 28)
print(x)
