from django.shortcuts import render
from myapp.serializer import *
from myapp.models import * 
from rest_framework.decorators import api_view,APIView
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser
from rest_framework.viewsets import ModelViewSet


class Userviewset(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = Userserializer

    def get_permissions(self):
        if self.action == "list":
            permission_classse = [AllowAny]

        elif self.action == "create":
            permission_classse = [AllowAny]

        elif  self.action == 'retrieve':
            permission_classse = [AllowAny]

        elif self.action == 'destroy':
            permission_classse = [AllowAny]

        elif self.action == 'update':
            permission_classse = [AllowAny]
                
        else:
            permission_classse = [IsAuthenticated]
        
        return [premission() for premission in permission_classse]

class Categoryviewset(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = Cateoryserializer

    def get_permissions(self):
        if self.action == "list":
            permission_classse = [AllowAny]

        elif self.action == "create":
            permission_classse = [AllowAny]

        elif  self.action == 'retrieve':
            permission_classse = [AllowAny]

        elif self.action == 'destroy':
            permission_classse = [AllowAny]

        elif self.action == 'update':
            permission_classse = [AllowAny]
                
        else:
            permission_classse = [IsAuthenticated]
        
        return [premission() for premission in permission_classse]

class Productviewset(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = Productserializer

    def get_permissions(self):
        if self.action == "list":
            permission_classse = [AllowAny]

        elif self.action == "create":
            permission_classse = [AllowAny]

        elif  self.action == 'retrieve':
            permission_classse = [AllowAny]

        elif self.action == 'destroy':
            permission_classse = [AllowAny]

        elif self.action == 'update':
            permission_classse = [AllowAny]
                
        else:
            permission_classse = [IsAuthenticated]
        
        return [premission() for premission in permission_classse]
