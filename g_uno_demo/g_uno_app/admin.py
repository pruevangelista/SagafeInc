from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Product)
admin.site.register(DeliveryReceipt)
admin.site.register(Client)
admin.site.register(QuantityOrdered)
