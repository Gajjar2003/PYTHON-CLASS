from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,APIView
from companyapp.models import *
from companyapp.serializer import *


class DeptAPI(APIView):

    def get(self,requset):
        depts = Dept.objects.all()
        ser = Deptserializer(depts,many=True)
        return Response({'data':ser.data})
    
    def post(self,requset):
        ser = Deptserializer(data= requset.data)
        if not ser.is_valid():
            return Response({'error':ser.errors})
        else:
            ser.save()
            return Response({'data':ser.data})
        

class DeptupdateAPI(APIView):

    def get(self,request,id):
        dept= Dept.objects.get(pk=id)
        ser = Deptserializer(dept)
        return Response({"data":ser.data})
    
    def delete(self,request,id):
        dept= Dept.objects.get(pk=id)
        dept.delete()
        return Response({"message":"dept deleted"})
    
    def put(self,request,id):
        dept= Dept.objects.get(pk=id)
        ser = Deptserializer(dept,request.data)
        if not ser.is_valid():
            return Response({"errors":ser.errors})
        else:
            ser.save()
            return Response({"data":ser.data})

@api_view(['POST'])
def addemp(request,id)  :
    data = request.data
    data.update({"dept":id})
    ser = Empserializer(data=data)
    if not ser.is_valid():
        return Response({"errors":ser.errors})
    else:
        ser.save()
        return Response({"data":ser.data})

@api_view(['GET'])    
def getemps(request):
    emps = Employee.objects.all()
    ser = Empserializer(emps,many=True)
    return Response({"data":ser.data})
    



