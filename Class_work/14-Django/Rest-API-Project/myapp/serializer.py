from rest_framework import serializers
from django.contrib.auth.models import User
from myapp.models import *

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields  = ['id','username','password']

    def create(self, validated_data):
        user =User.objects.create_user(**validated_data)
        return user

class Cateoryserializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields  = "__all__"

    def __str__(self):
        return self.name



class Productserializer(serializers.ModelSerializer):
    category = Cateoryserializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(),source='category',write_only=True)

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