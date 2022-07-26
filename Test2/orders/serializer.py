from rest_framework import serializers
from . models import Order,OrderItems



class OrderItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OrderItems
        fields = ('quentity','status','product')


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)
    class Meta:
        model = Order
        fields = ('number_order', 'order_items')
    
        
    
        
