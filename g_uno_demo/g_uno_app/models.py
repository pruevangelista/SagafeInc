from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import date, timedelta

# Create your models here.

#Product
class Product(models.Model):
    product_ID = models.IntegerField(validators=[MaxValueValidator(999999)], null=False, primary_key=True) #Random 
    product_name = models.CharField(max_length=55)
    code = models.CharField(max_length=3)
    type = models.CharField(max_length=30)
    size = models.CharField(max_length=20)
    unit = models.CharField(max_length=20)
    unit_price = models.DecimalField(max_digits=8, decimal_places=2, null=False)
    objects = models.Manager()

    def getProductID(self):
        return self.product_ID
    
    def getProductName(self):
        return self.product_name 
    
    def getCode(self):
        return self.code
    
    def getType(self):
        return self.type 

    def getSize(self):
        return self.size 
    
    def getUnit(self):
        return self.unit
    
    def getUnitPrice(self):
        return self.unit_price 
    
    def __str__(self):
        return ( 
            f"Product ID: {self.product_ID}, "
            f"Product Name: {self.product_name}, "
            f"Code: {self.code}, "
            f"Type: {self.type}, "
            f"Size: {self.size}, "
            f"Unit: {self.unit}, "
            f"Unit Price: {self.unit_price}"
        )


# Associative
class QuantityOrdered(models.Model):
    dr = models.ForeignKey("DeliveryReceipt", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def getDr(self):
        return self.dr
    
    def getQuantity(self):
        return self.quantity

#Delivery Receipt
class DeliveryReceipt(models.Model):
    dr_number = models.AutoField(primary_key=True)

    

    dr_date = models.DateField(null=False, default=date.today)
    dr_due_date = models.DateField(null=False, default=date.today)

    #ENUM: DR Terms
    terms = [
        ("90", "90"),
        ("120", "120")
    ]

    dr_terms = models.CharField(max_length=3, choices=terms, null=False)
    product_id = models.ManyToManyField(Product, through=QuantityOrdered, blank=True, null=False)

    dr_amt_wo_vat = models.FloatField(null=True, blank=True)
    dr_amt_vat = models.FloatField(null=True, blank=True)

    def getDrNumber(self):
        return self.product_id
    
    def getDrAmtVat(self):
        return self.dr_amt_vat

    def getDrAmtWoVat(self):
        return self.dr_amt_wo_vat
    
    def getDate(self):
        return self.dr_date

    def getDueDate(self):
        return self.dr_due_date
    
    def formatDrNumber(self):
        return "{:02d}-{:03d}".format(self.dr_number // 1000, self.dr_number % 1000)

    def __str__(self):
        return (
            f"DR Number: {self.dr_number}, "
        )
     


    


#Client
class Client(models.Model):
    client_ID = models.IntegerField(validators=[MaxValueValidator(999999)], null=False, primary_key=True) #Random
    client_name = models.CharField(max_length=55)
    client_address = models.CharField(max_length=255)
    client_TIN = models.CharField(max_length=15)
    objects = models.Manager()

    def clientID(self):
        return self.client_ID
    
    def clientName(self):
        return self.client_name
    
    def clientAddress(self):
        return self.client_address
    
    def clientTIN(self):
        return self.client_TIN
    
    def __str__(self):
        return (
            f"Client ID: {self.client_ID}, "
            f"Client Name: {self.client_name}, "
            f"Client Address: {self.client_address}, "
            f"Client TIN: {self.client_TIN}"
        )
    

#Check (Payment)
#Statement of Account (SOA)
