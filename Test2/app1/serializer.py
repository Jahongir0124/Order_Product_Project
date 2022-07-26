from rest_framework import serializers
from . models import Product
from django.contrib.auth.models import User

class ProductSerilzer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','name','price')
        
        
class ProductCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ('id','name','price')
        
    def create(self, validated_data):
        product = Product(
            name=validated_data['name'],
            price=validated_data['price']
        )
        product.save()
        return ''
    
class UserCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('username','email','password')
        
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return ''