from django.db import models

# Create your models here.

class Department(models.Model):
    Department_id = models.AutoField(primary_key=True)
    Department_Name = models.CharField(max_length=25)
    class Meta:
        db_table="Department"
class Employee(models.Model):

    Department =models.ForeignKey(Department,on_delete=models.CASCADE)
    Employee_id=models.AutoField(primary_key=True)
    Punch_Card_NO=models.IntegerField(unique=True)
    Name=models.CharField(max_length=25)
    Designation=models.CharField(max_length=30)
    Location=models.CharField(max_length=30)
    DOB=models.DateField()
    DOJ=models.DateField()
    DOL=models.DateField()
    Parents_Name=models.CharField(max_length=25)
    Martial_Status=models.CharField(max_length=25)
    Permanent_Address=models.TextField()
    Present_Address=models.TextField()
    Blood_Group=models.CharField(max_length=10)
    UAN_Number=models.IntegerField(null=True,unique=True)
    PF_PW=models.IntegerField()
    ESI_Number=models.IntegerField()
    Mobile_No=models.IntegerField()
    Email=models.EmailField(null=True)
    Aadhar_No=models.IntegerField()
    PAN=models.CharField(max_length=25)
    Bank_Acc_NO=models.IntegerField()
    IFSC_Code=models.CharField(max_length=25)
    Bank_Name=models.CharField(max_length=25)
    Emergency_Contact_No=models.IntegerField()
    Contact_No=models.IntegerField()
    Sur_name=models.CharField(max_length=25)
    Qualification=models.CharField(max_length=25)
    Experience=models.CharField(max_length=25)
    Remarks=models.TextField()
    Salary=models.IntegerField()
    class Meta:
        db_table="Employee"

class Attendance(models.Model):
    Employee=models.ForeignKey(Employee,on_delete=models.CASCADE)
    Attendance_id=models.AutoField(primary_key=True)
    Date = models.DateField()

    class Meta:
        db_table="Attendance"


class Item(models.Model):
    Item_id =  models.AutoField(primary_key=True)
    Item_Name = models.CharField(max_length = 20)
    class Meta:
        db_table="Item"
class Supplier(models.Model):
    Supplier_id = models.AutoField(primary_key=True)
    Supplier_Name = models.CharField(max_length=30)
    class Meta:
        db_table="Supplier"
class Product(models.Model):
    Product_id = models.AutoField(primary_key=True)
    Product_name = models.CharField(max_length=50)
    Item = models.ForeignKey(Item,on_delete=models.CASCADE)
    Supplier_id =models.ForeignKey(Supplier,on_delete=models.CASCADE)
    Quantity = models.IntegerField()
    Price = models.IntegerField()
    Purchase_Date = models.DateField()
    Invoice_Number = models.DateField()
    class Meta:
        db_table="Product"



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
