from django.db import models
class Contact_Db(models.Model):
    Name = models.CharField(max_length=100,blank=True,null=True)
    Email = models.EmailField(blank=True,null=True)
    Mobile = models.IntegerField(blank=True,null=True)
    Message = models.CharField(max_length=100,blank=True,null=True)

class Login_Db(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True)
    Email = models.EmailField(null=True,blank=True)
    Mobile = models.IntegerField(null=True,blank=True)
    Password = models.CharField(max_length=100,null=True,blank=True)
    Re_Password = models.CharField(max_length=100,null=True,blank=True)

class Cart_Db(models.Model):
    Quantity = models.IntegerField(blank=True,null=True)
    Price = models.IntegerField(blank=True,null=True)
    Total_Price = models.IntegerField(blank=True,null=True)
    Holder = models.CharField(max_length=100,null=True,blank=True)
    Name_Food = models.CharField(max_length=100,null=True,blank=True)
    Image_Food = models.CharField(max_length=255,null=True,blank=True)
class Order_Db(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True)
    Place = models.CharField(max_length=100,null=True,blank=True)
    Address = models.CharField(max_length=100,null=True,blank=True)
    State = models.CharField(max_length=100,null=True,blank=True)
    Order  = models.TextField(null=True,blank=True)
    Email = models.EmailField(null=True,blank=True)
    Mobile = models.IntegerField(null=True,blank=True)
    Country = models.CharField(max_length=100,null=True,blank=True)
    Code = models.IntegerField(null=True,blank=True)
    Total = models.IntegerField(null=True,blank=True)
