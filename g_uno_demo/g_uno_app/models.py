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
    
    def formatUnitPrice(self):
        return "{:,.2f}".format(self.unit_price)
    
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
    subtotal = models.FloatField(default=0)

    def getDr(self):
        return self.dr
    
    def getQuantity(self):
        return self.quantity
    
    def getSubtotal(self):
        return self.subtotal
    
    def formatSubtotal(self):
        return "{:,.2f}".format(self.subtotal)
    

#Delivery Receipt
class DeliveryReceipt(models.Model):
    dr_number = models.AutoField(primary_key=True)
    dr_date = models.DateField(null=False, default=date.today)
    dr_due_date = models.DateField(null=False, default=date.today)
    dr_vat = models.DecimalField(max_digits=8, decimal_places=2, null=False, default=0)

    #ENUM: DR Terms
    terms = [ 
        ("90", "90"),
        ("120", "120")
    ]

    dr_terms = models.CharField(max_length=3, choices=terms, null=False)
    client = models.ForeignKey("Client", on_delete=models.CASCADE, blank=True, null=False) #PRUE: Added this.
    product_id = models.ManyToManyField(Product, through=QuantityOrdered, blank=True, null=False)

    dr_amt_wo_vat = models.FloatField(null=False, blank=True, default = 0)
    dr_amt_vat = models.FloatField(null=False, blank=True, default = 0)

    #ENUM: DR Payment Status
    payment_status = [ 
        ("Not Paid", "Not Paid"),
        ("Partially Paid", "Partially Paid"),
        ("Fully Paid", "Fully Paid")
    ]

    dr_payment_status = models.CharField(max_length=15, choices=payment_status, default="Not Paid", null=False)

    def getDrNumber(self):
        return self.dr_number
    
    def getDrAmtVat(self):
        return "{:,.2f}".format(self.dr_amt_vat)

    def getDrAmtWoVat(self):
        return "{:,.2f}".format(self.dr_amt_wo_vat)
    
    def getDate(self):
        return self.dr_date

    def getDueDate(self):
        return self.dr_due_date
    
    def getTerms(self):
        return self.dr_terms
    
    def getPaymentStatus(self):
        return self.dr_payment_status
    
    def formatDrNumber(self):
        return "{:02d}-{:03d}".format(self.dr_number // 1000, self.dr_number % 1000)
    
    #Prue: Added this 
    def formatDate(self):
        return self.dr_date.strftime("%m/%d/%Y")

    def __str__(self):
        return (
            f"DR Number: {self.dr_number}"
        )
    
#Client
class Client(models.Model):
    client_ID = models.AutoField(primary_key=True) #Prue: Changed from IntegerField to AutoField. 
    client_name = models.CharField(max_length=55)
    client_address = models.CharField(max_length=255)
    client_TIN = models.CharField(max_length=15)
    objects = models.Manager()

    def getClientID(self):
        return self.client_ID
    
    def getClientName(self):
        return self.client_name
    
    def getClientAddress(self):
        return self.client_address
    
    def getClientTIN(self):
        return self.client_TIN
    
    # Prue: added this. 
    def formatClientTIN(self):
        # Split TIN into parts and create list 
        parts = [self.client_TIN[i:i + 3] for i in range(0, len(self.client_TIN), 3)]
        formatted_TIN = "-".join(parts)

        return formatted_TIN
    
    def __str__(self):
        return (
            f"Client ID: {self.client_ID}, "
            f"Client Name: {self.client_name}, "
            f"Client Address: {self.client_address}, "
            f"Client TIN: {self.formatClientTIN()}"
        )
    

#Check (Payment)
#Statement of Account (SOA)
