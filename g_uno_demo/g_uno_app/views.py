from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from decimal import Decimal
from .utils import *
from django.http import JsonResponse

# Create your views here.

def align_test(request):
    return render(request, 'g_uno_app/align_test.html')

def dr_home(request):
    deliveryReceipts = DeliveryReceipt.objects.all()
    context = {
        'drs': deliveryReceipts,
    }
    return render(request, 'g_uno_app/dr_home.html', context)

def new_dr(request):
    if(request.method == "POST"):
        # Client 
        inp_clientName = request.POST.get("TEST")
        inp_clientAddress = request.POST.get("clientaddress")
        inp_clientTIN = request.POST.get("clienttin")

        # DR
        inp_terms = request.POST.get("inputTerms")

        # Products
        inp_quantity = request.POST.getlist("quantity")
        inp_product = request.POST.getlist("input_productchoice")
        inp_size = request.POST.getlist("size")
        print(inp_size)

        # Instances
        #get_or_create() - https://www.letscodemore.com/blog/django-get-or-create/
        client_instance, created = Client.objects.get_or_create(
            client_name = inp_clientName, #Checks if client already exists 
            defaults = {"client_address": inp_clientAddress, "client_TIN": inp_clientTIN}
        )

        if created: 
            client_instance.save() 
        
        # Add products to DR
        dr_instance = DeliveryReceipt.objects.create(dr_terms=inp_terms, client=client_instance)
        dr_instance.dr_due_date = dr_instance.dr_date + timedelta(days=int(inp_terms))

        gen_subtotal = []
        for product_index in range(len(inp_quantity)):
            chosen_product = Product.objects.get(product_name__iexact = inp_product[product_index], size__iexact = inp_size[product_index])
            gen_subtotal.append(chosen_product.getUnitPrice() * Decimal(inp_quantity[product_index]))
            order_quantity_instance = QuantityOrdered.objects.create(dr = dr_instance, product = chosen_product, 
                                                                     quantity = inp_quantity[product_index], 
                                                                     subtotal = gen_subtotal[product_index])
            dr_instance.product_id.add(chosen_product)
            dr_instance.save()
            
        
        dr_instance.dr_amt_vat = sum(gen_subtotal)
        dr_instance.dr_amt_wo_vat = round(sum(gen_subtotal) / Decimal(1.12), 2)
        dr_instance.save()
        dr_instance.dr_vat = dr_instance.dr_amt_vat - dr_instance.dr_amt_wo_vat
        dr_instance.save()
        

        context = {
            'a':chosen_product,
            'b': order_quantity_instance,
            'c': dr_instance,
            'd': client_instance,
        }

        return redirect('view_dr', pk=dr_instance.pk)
    else:
        print("AAAAAwdasdawdA")
        return render(request, 'g_uno_app/new_dr.html') 

def add_dr(request):    
    new_DRnumber = get_next(DeliveryReceipt)
    # Saves new_DRnumber only in memory until user actually clicks the confirm button in add_dr.html 
    dr_instance = DeliveryReceipt(dr_number=new_DRnumber)
    allProducts = Product.objects.all()
    context = {
        'c': dr_instance,
        'p': allProducts
    }
    return render(request, 'g_uno_app/add_dr.html', context)

def view_dr(request, pk):
    dr = get_object_or_404(DeliveryReceipt, pk=pk)
    qps = QuantityOrdered.objects.filter(dr=dr)
    context = {
        'qps': qps,
        'dr': dr
    }
    # for i in deliveryReceipts:
    #     print(i.getDrNumber())
    return render(request, 'g_uno_app/view_dr.html', context)


def get_price(request, pk):
    products = Product.objects.get(pk=pk)
    return JsonResponse({'price': str(products.unit_price) })

def get_prod_id(request):
    prod_name = request.GET.get('input_productchoice')
    product = Product.objects.get(product_name=prod_name)
    print("ASDAWDASD")
    print(product)
    return JsonResponse({'id': product.product_ID})