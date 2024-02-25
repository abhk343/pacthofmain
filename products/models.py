from django.db import models
from home.models import *
# Create your models here.

class Item(models.Model):
    Item_id =  models.AutoField(primary_key=True)
    Item_Name = models.CharField(max_length = 20)
    class Meta:
        db_table="Item"
    
    def __str__(self):
        return self.Item_Name

class Supplier(models.Model):
    Supplier_id = models.AutoField(primary_key=True)
    Supplier_Name = models.CharField(max_length=30)
    class Meta:
        db_table="Supplier"
    def __str__(self):
        return self.Supplier_Name
        
class Product(models.Model):
    Product_id = models.AutoField(primary_key=True)
    Product_name = models.CharField(max_length=50)
    Item = models.ForeignKey(Item,on_delete=models.CASCADE)
    Supplier =models.ForeignKey(Supplier,on_delete=models.CASCADE)
    Quantity = models.IntegerField()
    Price = models.IntegerField()
    Purchase_Date = models.DateField()
    Invoice_Number = models.IntegerField()
    class Meta:
        db_table="Product"
        
    def __str__(self):
        return self.Product_name
        



class Stock_in(models.Model):
    Stock_in_id = models.AutoField(primary_key=True)
    Item= models.ForeignKey(Item,on_delete=models.CASCADE)
    Quantity_available = models.IntegerField()
    Date_added = models.DateField()
    class Meta:
        db_table="Stock_in"

class Stock_out(models.Model):
    Stock_out_id = models.AutoField(primary_key=True)
    Employee=models.ForeignKey(Employee,on_delete=models.CASCADE)
    Item_id = models.ForeignKey(Item,on_delete=models.CASCADE)
    Quantity_given = models.IntegerField()
    Date_given = models.DateField()
    class Meta:
        db_table="Stock_out"
