from django.db import models

class Style_Db(models.Model):
    Food_Style = models.CharField(max_length=100,blank=True,null=True)
    Description = models.CharField(max_length=100,blank=True,null=True)
    Style_Image = models.ImageField(upload_to="Styles",blank=True,null=True)

class Food_Db(models.Model):
    Style = models.CharField(max_length=100,blank=True,null=True)
    Food_Name = models.CharField(max_length=100,blank=True,null=True)
    Food_Description = models.CharField(max_length=100,blank=True,null=True)
    Quantity = models.IntegerField(blank=True,null=True)
    MRP = models.IntegerField(blank=True,null=True)
    Image1 = models.ImageField(upload_to="Foods",blank=True,null=True)
    Image2 = models.ImageField(upload_to="Foods",blank=True,null=True)





# Create your models here.
