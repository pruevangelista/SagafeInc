from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from decimal import Decimal

# Create your views here.

# def test(request):
#     drs = dr_test.objects.all()
#     return render(request, 'gu_app/test.html', {"drs": drs})

# def test_submit(request):
#     if(request.method == "POST"):
#         inp_number = request.POST.get('dr_number')
#         inp_date = request.POST.get('dr_date')
#         inp_terms = request.POST.get('dr_terms')
        

#         dr_test.objects.create(dr_number = inp_number, dr_date = inp_date, dr_terms = inp_terms)
#         return redirect('test')
#     else:
#         return render(request, 'gu_app/test.html')


def dr_home(request):
    return render(request, 'g_uno_app/dr_home.html')

def add_dr(request):
    # Checks if the latest DR instance exists and retrieves its dr_number
    if DeliveryReceipt.objects.exists(): 
        latest_DRinstance = DeliveryReceipt.objects.latest('dr_number')
        latest_DRnumber = latest_DRinstance.dr_number 
        new_DRnumber = latest_DRnumber + 1 
    else: 
        new_DRnumber = 1

    # Saves new_DRnumber only in memory until user actually clicks the confirm button in add_dr.html 
    dr_instance = DeliveryReceipt(dr_number=new_DRnumber)

    context = {
        'c': dr_instance,
        #'d': client_instance, (for suggested client_name inputs)
        #'e': product_instance, (for suggested product_name inputs)
    }
    return render(request, 'g_uno_app/add_dr.html', context)

def new_dr(request):
    if(request.method == "POST"):
        

        # Lists
        tet = request.POST.getlist('quantity')
        x = request.POST.getlist('productchoice')
        
        # tet = request.POST.get('clienttin')
        print(tet)
        print(x)
    #     inp_terms = request.POST.get("terms")

    #     # Products
    #     inp_quantity = request.POST.getlist("inp_quantity[]")
    #     inp_product = request.POST.getlist("inp_product[]")
    #     inp_size = request.POST.getlist("inp_size[]")

    #     # Instances
    #     dr_instance = DeliveryReceipt.objects.create(dr_terms=inp_terms)
    #     dr_instance.dr_due_date = dr_instance.dr_date + timedelta(days=int(inp_terms))

    #     gen_subtotal = []
    #     for product_index in range(len(inp_quantity)):
    #         chosen_product = Product.objects.get(product_name__iexact = inp_product[product_index], size__iexact = inp_size[product_index])
    #         gen_subtotal.append(chosen_product.getUnitPrice() * Decimal(inp_quantity[product_index]))
    #         order_quantity_instance = QuantityOrdered.objects.create(dr = dr_instance, product = chosen_product, 
    #                                                                  quantity = inp_quantity[product_index], 
    #                                                                  subtotal = gen_subtotal[product_index])
    #         dr_instance.product_id.add(chosen_product)
    #         dr_instance.save()
            



    #     dr_instance.dr_amt_wo_vat = sum(gen_subtotal)
    #     dr_instance.dr_amt_vat = round(sum(gen_subtotal) * Decimal(1.12), 2)
    #     dr_instance.save()

    #     context = {
    #         'a':chosen_product,
    #         'b': order_quantity_instance,
    #         'c': dr_instance,
    #     }

        return render(request, 'g_uno_app/new_dr.html') #implement pk 
    else:
        print("AAAAAA")
        return render(request, 'g_uno_app/new_dr.html') #implement pk 

def add_dr_lar(request):
    return render(request, 'g_uno_app/add_dr_lar.html')