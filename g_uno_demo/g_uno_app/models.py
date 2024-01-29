from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

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

#Delivery Receipt
class DeliveryReceipt(models.Model):
    dr_number = models.IntegerField(validators=[MaxValueValidator(99999)], null=False, primary_key=True) #Auto-increment, FORMAT: 00-000
    dr_date = models.DateField(null=False, auto_now_add=True)
    #ENUM: DR Terms
    terms = [
        ("90", "90"),
        ("120", "120")
    ]
    dr_terms = models.CharField(max_length=3, choices=terms, null=False)
    dr_vat = models.DecimalField(max_digits=8, decimal_places=2, null=False)
    dr_amtwvat = models.DecimalField(max_digits=8, decimal_places=2, null=False)
    dr_amtwovat = models.DecimalField(max_digits=8, decimal_places=2, null=False)
    dr_subtotal = models.DecimalField(max_digits=8, decimal_places=2, null=False)
    dr_duedate = models.DateField(null=False)
    #ENUM: Payment Status
    payment_status = [
        ("Not Paid", "Not Paid"),
        ("Partially Paid", "Partially Paid"),
        ("Fully Paid", "Fully Paid")
    ]
    dr_paymentstatus = models.CharField(max_length=15, choices=payment_status, null=False)
    #client_id = models.ForeignKey(Client, on_delete=models.CASCADE, db_constraint=False, db_column='client_id_number')
    #SOA_number = models.ForeignKey(SOA, on_delete=models.CASCADE, db_constraint=False, db_colum='SOA')
    objects = models.Manager()

    def getDRNumber(self):
        return self.dr_number
    
    def getDRDate(self):
        return self.dr_date
    
    def getDRTerms(self):
        return self.dr_terms 
    
    def getVAT(self):
        return self.dr_vat
    
    def getWVAT(self):
        return self.dr_amtwvat
    
    def getWOVAT(self):
        return self.dr_amtwovat
    
    def getSubtotal(self):
        return self.dr_subtotal
    
    def getDueDate(self):
        return self.dr_duedate
    
    def getPaymentStatus(self):
        return self.dr_paymentstatus
    
    def __str__(self):
        return (
            f"DR Number: {self.dr_number}, "
            f"Date: {self.dr_date}, "
            f"Terms: {self.dr_terms}, "
            f"VAT: {self.dr_vat}, "
            f"WVAT: {self.dr_amtwvat}, "
            f"WOVAT: {self.dr_amtwovat}, "
            f"Subtotal: {self.dr_subtotal}, "
            f"Due Date: {self.dr_duedate}, "
            f"Payment Status: {self.dr_paymentstatus}"
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
