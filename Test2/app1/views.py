from django.http import Http404
from django.shortcuts import render
from numpy import delete
from rest_framework.views import APIView
from rest_framework.response import Response
from . serializer import ProductSerilzer,ProductCreateSerializer,UserCreateSerializer
from . models import Product
from rest_framework import authentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
# Create your views here.


class ProductView(APIView):
    serializer_class = ProductSerilzer
    
    def get(self,request):
        
        product = Product.objects.all()
        serializer_date = self.serializer_class(product,many=True)
        return Response(serializer_date.data)

class ProductCreate(APIView):
    serializer_class =  ProductCreateSerializer
    permission_classes = [IsAdminUser]
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        product = serializer.save()
        return Response({
            "Product created Sucsess"

        })
        
class ProductDetail(APIView):
    permission_classes = [IsAdminUser]
    def get_object(self,pk):
        try:
            return Product.objects.get(pk=pk)
        except Exception as e:
            raise Http404
    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerilzer(product)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):        
        product = self.get_object(pk)
        serializer = ProductSerilzer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response('Updated Data')
    def delete(self, request,pk,format=None):
        product = self.get_object(pk)
        product.delete()
        return Response('Deleted Data')
    
class RegistrationView(APIView):
    serializer_class =  UserCreateSerializer
    
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        teacher = serializer.save()
        return Response({
            "user created Sucsess"

        })

    
    

    
    



