from django.http import Http404
from django.shortcuts import render
from  .models import Order, OrderItems
from drf_yasg.utils import swagger_auto_schema
from  .serializer import OrderItemSerializer, OrderSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAdminUser
# # Create your views here.

class OrderView(APIView):
    
    serializer_class =  OrderSerializer
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(request_body=OrderSerializer)
    def post(self,request,*args,**kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        order = Order(
                customer=request.user,
            )
        order.save()
        for i in serializer.data['order_items']:
            ord_items = OrderItems(
                product_id=i['product'],
                order=order,
                quentity=i['quentity']
            )
            ord_items.save()
        return Response('Ok')



