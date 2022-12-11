from django.db import models
from customers.models import customer
from suppliers.models import supplier

# Create your models here.
class product(models.Model):
    name = models.CharField(max_length=100)
    avg_price = models.DecimalField(decimal_places=2,default=0, max_digits=5)
    available_qty = models.IntegerField(default=0)
    pending_qty = models.IntegerField(default=0) 
    status = models.IntegerField(default=1)

class invoice(models.Model):
    date = models.DateField()
    customer = models.ForeignKey(customer, on_delete=models.DO_NOTHING)
    products_count = models.IntegerField()
    total = models.IntegerField()
    delivery_status = models.SmallIntegerField()
    payment_status = models.SmallIntegerField()

class invoice_product(models.Model):
    invoice = models.ForeignKey(invoice, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.DO_NOTHING)
    unit_price = models.IntegerField()
    weight = models.IntegerField()
    total = models.IntegerField()

class import_invoice(models.Model):
    date = models.DateField()
    supplier = models.ForeignKey(supplier, on_delete=models.DO_NOTHING)
    products_count = models.IntegerField()
    total = models.IntegerField()
    load_status = models.SmallIntegerField(default=0)
    payment_status = models.SmallIntegerField(default=0)
    status = models.SmallIntegerField(default=0)
    invoice_image = models.ImageField(upload_to='static/img/invoices/',default='static/img/invoices/default.jpg')

class import_product(models.Model):
    invoice = models.ForeignKey(import_invoice, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.DO_NOTHING)
    unit_price = models.IntegerField()
    weight = models.IntegerField()
    total = models.IntegerField()