import imp
import json
from django.shortcuts import HttpResponse, render, redirect
from django.contrib import messages
from django.db.models import Sum
from .models import product,invoice,invoice_product,import_invoice,import_product
from .forms import ProductForm 
from django.http import JsonResponse
from django.core import serializers
from customers.models import customer
from suppliers.models import supplier


# Create your views here.

def products(request):
    if request.method == 'POST':
        form  = ProductForm(request.POST) 
        if form.is_valid():
            cd = form.cleaned_data
            pc = product(
                name = cd['name'] 
            )
            pc.save() 
            messages.success(request, 'Product created : ' + cd['name'])
            return redirect('products')
        else:
            print('Form is not valid')
            messages.error(request, 'Error Processing Your Request') 
            form  = ProductForm() 
            products = product.objects.order_by('id').all()
            count = products.count()
            return render(request,'products.html',{'nbar': 'products','products':products,'form': form,'count':count})
    if request.method == 'GET':
        form  = ProductForm() 
        products = product.objects.order_by('id').all()
        count = products.count()
        totals = products.aggregate(Sum('available_qty'),Sum('pending_qty'))
        return render(request,'products.html',{'nbar': 'products','products':products,'form': form,'count':count,'totals':totals}) 

def invoices(request):
    customers = customer.objects.all() 
    return render(request,'invoices.html',{'nbar': 'invoices','customers':customers}) 

def invoice_data(request):
    # invoices = invoice.objects.all() 
    # post_list = serializers.serialize('json', invoices)
    # return JsonResponse(post_list, safe=False)
    delivery_status = int(request.GET['delivery_status']) 
    payment_status = int(request.GET['payment_status']) 
    customer_id = int(request.GET['customer']) 
    startdate = request.GET['startdate']
    enddate = request.GET['enddate']

    # if(request.GET['customer'] > 0):
    #     customerQuery = ''
    
    obj = invoice.objects.all().values('id','date','products_count','total','delivery_status','payment_status','customer__name')
    
    if delivery_status > -1 :
        obj = obj.filter(delivery_status=delivery_status)

    if payment_status > -1 :
        obj = obj.filter(payment_status=payment_status)

    if customer_id > 0 :
        customerr = customer.objects.get(id=customer_id)
        obj = obj.filter(customer=customerr)
    
    if startdate != '' :
        obj = obj.filter(date__gte=startdate)

    if enddate != '' :
        obj = obj.filter(date__lte=enddate)

    return JsonResponse({'data':list(obj)})

def create_invoice(request):
    if request.method == 'GET': 
        customers = customer.objects.all()
        products = product.objects.order_by('id').all()  
        return render(request,'create-invoice.html',{'nbar': 'create-invoice','customers':customers,'products':products}) 

def insert_invoice(request):
    if request.method == 'POST':
        date = request.POST['date']
        customer_id = request.POST['customer']
        count = request.POST['count']
        total = request.POST['total']
        customer_data = customer.objects.get(id=customer_id)
        invoice_data = invoice(
            date = date,
            customer = customer_data,
            products_count = count,
            total = total,
            delivery_status = 0,
            payment_status = 0
        ) 
        invoice_data.save()
        items = json.loads(request.POST['items'])
        for item in items:
            product_id = item['id']
            qty = int(item['qty'])
            price = int(item['price'])
            total = qty*price
            product_data = product.objects.get(id=product_id)
            invoice_product_data = invoice_product(
                invoice = invoice_data,
                product = product_data,
                unit_price = price,
                weight = qty,
                total = total
            ) 
            invoice_product_data.save()
        return HttpResponse(items)

def invoice_details(request, id):
    invoice_data = invoice.objects.get(id=id)
    invoice_product_data = invoice_product.objects.all().filter(invoice=invoice_data)
    return render(request,'invoice.html',{'invoice':invoice_data,'items':invoice_product_data})

def imports(request):
    suppliers = supplier.objects.all() 
    return render(request, 'imports.html',{'nbar':'imports','suppliers':suppliers})

def import_invoice_data(request):
    load_status = int(request.GET['load_status']) 
    payment_status = int(request.GET['payment_status']) 
    supplier_id = int(request.GET['supplier']) 
    startdate = request.GET['startdate']
    enddate = request.GET['enddate']
    
    obj = import_invoice.objects.all().values('id','date','products_count','total','load_status','payment_status','supplier__name')
    
    if load_status > -1 :
        obj = obj.filter(load_status=load_status)

    if payment_status > -1 :
        obj = obj.filter(payment_status=payment_status)

    if supplier_id > 0 :
        supplierr = supplier.objects.get(id=supplier_id)
        obj = obj.filter(supplier=supplierr)
    
    if startdate != '' :
        obj = obj.filter(date__gte=startdate)

    if enddate != '' :
        obj = obj.filter(date__lte=enddate)

    return JsonResponse({'data':list(obj)})

def import_products(request):
    suppliers = supplier.objects.order_by('id').all() 
    products = product.objects.order_by('id').all()
    return render(request, 'import-products.html',{'nbar':'import-products','suppliers':suppliers,'products':products})

def import_invoice_products_data(request):
    load_status = int(request.GET['load_status']) 
    payment_status = int(request.GET['payment_status']) 
    supplier_id = int(request.GET['supplier']) 
    startdate = request.GET['startdate']
    enddate = request.GET['enddate']
    
    # obj = import_invoice.objects.all().values('id','date','products_count','total','load_status','payment_status','supplier__name')
    obj = import_product.objects.all().values('invoice__id','invoice__date','product__name','unit_price','weight','total','invoice__supplier__name','invoice__load_status','invoice__payment_status')
    # if load_status > -1 :
    #     obj = obj.filter(load_status=load_status)

    # if payment_status > -1 :
    #     obj = obj.filter(payment_status=payment_status)

    # if supplier_id > 0 :
    #     supplierr = supplier.objects.get(id=supplier_id)
    #     obj = obj.filter(supplier=supplierr)
    
    # if startdate != '' :
    #     obj = obj.filter(date__gte=startdate)

    # if enddate != '' :
    #     obj = obj.filter(date__lte=enddate)

    return JsonResponse({'data':list(obj)})

def add_import_invoice(request):
     if request.method == 'GET': 
        suppliers = supplier.objects.all()
        products = product.objects.order_by('id').all()  
        return render(request,'create-import-invoice.html',{'nbar': 'create-import-invoice','suppliers':suppliers,'products':products}) 

def insert_import_invoice(request):
    if request.method == 'POST':
        date = request.POST['date']
        supplier_id = request.POST['supplier']
        count = request.POST['count']
        total = request.POST['total']
        image = request.FILES['image']
        supplier_data = supplier.objects.get(id=supplier_id)
        invoice_data = import_invoice(
            date = date,
            supplier = supplier_data,
            products_count = count,
            total = total,
            load_status = 0,
            payment_status = 0,
            invoice_image = image
        ) 
        invoice_data.save()
        items = json.loads(request.POST['items'])
        for item in items:
            product_id = item['id']
            qty = int(item['qty'])
            price = int(item['price'])
            total = qty*price
            product_data = product.objects.get(id=product_id)
            invoice_product_data = import_product(
                invoice = invoice_data,
                product = product_data,
                unit_price = price,
                weight = qty,
                total = total
            ) 
            invoice_product_data.save()
        return JsonResponse({'url':invoice_data.invoice_image.url}) 