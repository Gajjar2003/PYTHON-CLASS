from rest_framework import serializers
from django.contrib.auth.models import User
from myapp.models import *

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields  = "__all__"


class Cateoryserializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields  = "__all__"


class Productserializer(serializers.ModelSerializer):
    class Meta:
        model  = Product
        fields = "__all__"



class Addressserializer(serializers.ModelSerializer):
    class Meta:
        model  = Address
        fields = "__all__"



class Cartserializer(serializers.ModelSerializer):
    class Meta:
        model  = Cart
        fields = "__all__"


class CartItemserializer(serializers.ModelSerializer):
    class Meta:
        model  = CartItem
        fields = "__all__"

class Orderserializer(serializers.ModelSerializer):
    class Meta:
        model  = Order
        fields = "__all__"


class OrderItemserializer(serializers.ModelSerializer):
    class Meta:
        model = OredrItem
        fields = "__all__"