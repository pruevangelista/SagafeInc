from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from .models import *

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
    return render(request, 'g_uno_app/add_dr.html')

def new_dr(request):
    return render(request, 'g_uno_app/new_dr.html') #implement pk 