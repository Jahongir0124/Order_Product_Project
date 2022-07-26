from turtle import mode
from django.db import models
from app1.models import Product
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

# Create your models here.


class Order(models.Model):
    class OrderStatus(models.TextChoices):
        PENDING = 'PENDING', 'PENDING'
        ON_WAY = 'CANCEL', 'CANCEL'
        DELIVIRED = 'DELIVIRED', 'DELIVERED'
        
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    number_order = models.AutoField(primary_key=True)
    created_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=30, choices=OrderStatus.choices, default=OrderStatus.PENDING)
    
    


class OrderItems(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quentity = models.IntegerField(default=1)
    status = models.BooleanField(default=False)
    
    
    
    
    


    

    
    
    



    
    
    
   
    
        
