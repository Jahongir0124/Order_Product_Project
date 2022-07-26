from pyexpat import model
from tabnanny import verbose
from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=300)
    price = models.IntegerField(default=0)
    data_created = models.DateTimeField(auto_now_add=True)
    updated_data = models.DateTimeField(auto_now=True)
    image = models.ImageField()
    
    def __str__(self):
        return self.name
    
    
    class Meta:
        verbose_name = 'Mahsulotlar ro\'yxati'
        verbose_name_plural = 'Mahsulotlar'
    
    
    
