from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import *
# Create your views here.
def Item_in(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('sucessfully submited')
    else:
        form = ItemForm()
    return render(request,'products/items_in.html',{'forms':form})

def item_view(request):
    items = Item.objects.all()
    return render(request,'products/items_view.html',{'item':items})

def supplier_in(request):
    if request.method == 'POST':
        forms = suppllierform(request.POST)
        if forms.is_valid():
            forms.save()
            return HttpResponse('sucessfully submited')
    else:
            forms=suppllierform()
            
    return render(request,'products/supplier_in.html',{'form':forms})

def supplier_view(request):
    supplier = Supplier.objects.all()
    return render(request,'products/supplier_view.html',{'suppliers':supplier})

def product_in(request):
    if request.method == 'POST':
        forms = productsform(request.POST)
        if forms.is_valid:  # Added parentheses after is_valid
            forms.save()
            return HttpResponse('Form submitted successfully')
    else:
        forms = productsform()
    
    return render(request, 'products/product_in.html', {'form': forms})

def product_view(request):
    products = Product.objects.all()
    return render(request,'products/product_view.html',{'product':products})