from django.shortcuts import render
from rest_framework.views import APIView
from orders.models import Order, OrderItems
from app1.models import Product
import zoneinfo
from django.utils.dateparse import parse_datetime
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAdminUser
# Create your views here.

class Profile(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        order = Order.objects.filter(customer=request.user)
        a = []
        
        
        for ord in order:
            total = 0
            product_items = []
            
            d = {}
            d = {
                'order_number':ord.number_order,
                'order_date':ord.created_date.strftime("%d.%m.%Y %H:%M"),
                'order_status':ord.status
            }
            try:
                ord_items = OrderItems.objects.filter(order_id=ord.pk)
            except Exception as e:
                print(e)
            for item in ord_items:
                g = {
                    'product_name':item.product.name,
                    'quentity':item.quentity,
                    'price':item.product.price,
                    
                }
                total+=g['price']*g['quentity']
                product_items.append(g)
            d['order_items'] = product_items
            d['total'] = total
            a.append(d)
        
        
        return Response(a)
        