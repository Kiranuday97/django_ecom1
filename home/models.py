from datetime import datetime
from decimal import Decimal
from typing import Self
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse




class Occasion(models.Model):
        type = models.CharField(max_length = 100)
        
        def __str__(self):
            return self.type    

class Products(models.Model):
        title = models.CharField(max_length=200)
        varient = models.CharField(max_length=200)
        description = models.CharField(max_length=300)
        price = models.PositiveBigIntegerField()
        image = models.ImageField(upload_to ='uploads')
        Occasion = models.ForeignKey(Occasion,on_delete=models.CASCADE)
        user = models.ForeignKey(User, on_delete=models. CASCADE,null=True)

        


        def __str__(self):
            return self.title  
        
class AddProduct(models.Model):
    Occasion = models.ForeignKey(Occasion,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    varient = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to ='products')
    
    
    def __str__(self):
         return self.title         
        



class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Products)
    total_price = models.DecimalField(decimal_places=2, max_digits=8)
    created_at = models.DateTimeField(auto_now_add=True)    



# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     product = models.ForeignKey(Products, on_delete=models.CASCADE)
#     quantity = models.IntegerField()
#     price = models.DecimalField(max_digits=6, decimal_places=2)
