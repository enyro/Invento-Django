import imp
import json
from django.shortcuts import HttpResponse, render, redirect
from django.contrib import messages
from django.db.models import Sum
from .models import Product,Invoice,InvoiceProduct,ImportInvoice,ImportProduct 
from django.http import JsonResponse
from django.core import serializers
from customers.models import Customer
from suppliers.models import Supplier

def products(request):   
    products = Product.objects.order_by('id').all()
    count = products.count()
    totals = products.aggregate(Sum('available_qty'),Sum('pending_qty'))
    return render(request,'products.html',{'nbar': 'products','count':count,'totals':totals}) 

def invoices(request):
    customers = Customer.objects.all() 
    return render(request,'invoices.html',{'nbar': 'invoices','customers':customers}) 

def invoice_data(request): 
    delivery_status = int(request.GET['delivery_status']) 
    payment_status = int(request.GET['payment_status']) 
    customer_id = int(request.GET['customer']) 
    startdate = request.GET['startdate']
    enddate = request.GET['enddate'] 
    
    obj = Invoice.objects.all().values('id','date','products_count','total','delivery_status','payment_status','customer__name','delivery_date')
    
    if delivery_status > -1 :
        obj = obj.filter(delivery_status=delivery_status)

    if payment_status > -1 :
        obj = obj.filter(payment_status=payment_status)

    if customer_id > 0 :
        customerr = Customer.objects.get(id=customer_id)
        obj = obj.filter(customer=customerr)
    
    if startdate != '' :
        obj = obj.filter(date__gte=startdate)

    if enddate != '' :
        obj = obj.filter(date__lte=enddate)

    return JsonResponse({'data':list(obj)})

def create_invoice(request):
    if request.method == 'GET': 
        customers = Customer.objects.all()
        products = Product.objects.order_by('id').all()  
        return render(request,'create-invoice.html',{'nbar': 'create-invoice','customers':customers,'products':products}) 

def insert_invoice(request):
    if request.method == 'POST':
        date = request.POST['date']
        customer_id = request.POST['customer']
        count = request.POST['count']
        total = request.POST['total']
        deliveryDate = request.POST['deliveryDate']
        customer_data = Customer.objects.get(id=customer_id)
        invoice_data = Invoice(
            date = date,
            customer = customer_data,
            products_count = count,
            total = total,
            delivery_status = 0,
            payment_status = 0,
            delivery_date = deliveryDate
        ) 
        invoice_data.save()
        items = json.loads(request.POST['items'])
        for item in items:
            product_id = item['id']
            qty = int(item['qty'])
            price = int(item['price'])
            total = qty*price
            product_data = Product.objects.get(id=product_id)
            invoice_product_data = InvoiceProduct(
                invoice = invoice_data,
                product = product_data,
                unit_price = price,
                weight = qty,
                total = total
            ) 
            invoice_product_data.save()
        return JsonResponse({'id': 200, 'data': invoice_data.id})

def invoice_details(request, id):
    invoice_data = Invoice.objects.get(id=id)
    invoice_product_data = InvoiceProduct.objects.all().filter(invoice=invoice_data)
    return render(request,'invoice.html',{'invoice':invoice_data,'items':invoice_product_data})

def imports(request):
    suppliers = Supplier.objects.all() 
    return render(request, 'imports.html',{'nbar':'imports','suppliers':suppliers})

def import_invoice_data(request):
    load_status = int(request.GET['load_status'])
    payment_status = int(request.GET['payment_status']) 
    supplier_id = int(request.GET['supplier']) 
    startdate = request.GET['startdate']
    enddate = request.GET['enddate']
    status = request.GET['status']
    
    obj = ImportInvoice.objects.all().values('id','date','products_count','total','status','load_status','payment_status','invoice_image','supplier__name').filter(status=status)
    
    if load_status > -1 :
        obj = obj.filter(load_status=load_status)

    if payment_status > -1 :
        obj = obj.filter(payment_status=payment_status)

    if supplier_id > 0 :
        supplierr = Supplier.objects.get(id=supplier_id)
        obj = obj.filter(supplier=supplierr)
    
    if startdate != '' :
        obj = obj.filter(date__gte=startdate)

    if enddate != '' :
        obj = obj.filter(date__lte=enddate)


    return JsonResponse({'data':list(obj)})

def import_products(request):
    suppliers = Supplier.objects.order_by('id').all() 
    products = Product.objects.order_by('id').all()
    return render(request, 'import-products.html',{'nbar':'import-products','suppliers':suppliers,'products':products})

def import_invoice_products_data(request):
    load_status = int(request.GET['load_status']) 
    payment_status = int(request.GET['payment_status']) 
    supplier_id = int(request.GET['supplier']) 
    startdate = request.GET['startdate']
    enddate = request.GET['enddate']
    
    # obj = import_invoice.objects.all().values('id','date','products_count','total','load_status','payment_status','supplier__name')
    obj = ImportProduct.objects.all().values('invoice__id','invoice__date','product__name','unit_price','weight','total','invoice__supplier__name','invoice__load_status','invoice__payment_status')
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
        suppliers = Supplier.objects.all()
        products = Product.objects.order_by('id').all()  
        return render(request,'create-import-invoice.html',{'nbar': 'create-import-invoice','suppliers':suppliers,'products':products}) 

def insert_import_invoice(request):
    if request.method == 'POST':
        date = request.POST['date']
        supplier_id = request.POST['supplier'] 
        count = request.POST['count']
        total = request.POST['total']
        image = request.FILES['image']
        arrivalDate = request.POST['arrivalDate']
        supplier_data = Supplier.objects.get(id=supplier_id)
        invoice_data = ImportInvoice(
            date = date,
            supplier = supplier_data,
            products_count = count,
            total = total, 
            invoice_image = image,
            arrival_date = arrivalDate
        ) 
        invoice_data.save()
        items = json.loads(request.POST['items'])
        for item in items:
            product_id = item['id']
            qty = int(item['qty'])
            price = int(item['price'])
            total = qty*price
            product_data = Product.objects.get(id=product_id)
            invoice_product_data = ImportProduct(
                invoice = invoice_data,
                product = product_data,
                unit_price = price,
                weight = qty,
                total = total
            ) 
            invoice_product_data.save()
        return JsonResponse({'url':invoice_data.invoice_image.url}) 

def update_invoice_delivery(request):
    invoice_id = request.POST['id']
    invoice_delivery_status = request.POST['status']

    invoice_update = Invoice.objects.get(id=invoice_id)
    invoice_update.delivery_status = invoice_delivery_status
    invoice_update.save()

    return JsonResponse({'id':200 , 'data':"Delivery status updated successfully!!"})

def pending_imports(request):
    return render(request, 'pending-imports.html',{'nbar': 'pending-import-invoice'})

def products_data(request):
    obj = Product.objects.all().values('id','name','available_qty','pending_qty','status') 
    return JsonResponse({'data':list(obj)})

def insert_product(request): 
    product = Product(
        name = request.POST['name']
    )
    product.save()
    return JsonResponse({'id':200 , 'data':"Product created successfully!!"})

def editProduct(request):
    id = request.POST['id']
    status = request.POST['status']

    product =Product.objects.get(pk=id)
    product.status = status
    product.save()
    return JsonResponse({'id':200 , 'data':"Product updated successfully!!"})

def update_invoice_payment(request):
    invoice_id = request.POST['id']
    invoice_payment_status = request.POST['status']

    invoice_update = Invoice.objects.get(id=invoice_id)
    invoice_update.payment_status = invoice_payment_status
    invoice_update.save()

    return JsonResponse({'id':200 , 'data':"Payment status updated successfully!!"})

def updateImportStatus(response):
    id = response.POST['id']
    status = response.POST['status']

    importInvoice = ImportInvoice.objects.get(pk=id)
    importInvoice.status = status
    importInvoice.save()

    return JsonResponse({'id':200,'data':"Status updated successfully!!"})