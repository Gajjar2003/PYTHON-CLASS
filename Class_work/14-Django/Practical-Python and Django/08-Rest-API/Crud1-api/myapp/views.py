from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from myapp.models import * 
from myapp.serializer import *


@api_view(['GET'])
def view(request):
    employee = Employee.objects.all()
    ser = Empployeeserializer(employee,many=True)
    return Response(ser.data)

@api_view(['POST'])
def add(request):
    sdata = request.data
    ser = Empployeeserializer(data=sdata)
    if not ser.is_valid():
        return Response({'data':ser.errors,"errors":"something went wrong"})
    else:
        ser.save()
        return Response({"data":ser.data,"message":"Employee data inserted in tables"})
    
@api_view(['GET'])
def getbyid(request,id):
    employee = Employee.objects.get(pk=id)
    ser = Empployeeserializer(employee)
    return Response({"data":ser.data})


@api_view(['PUT'])
def put(request,id):
    sdata = request.data
    cdata = Employee.objects.get(pk=id)
    ser = Empployeeserializer(cdata,sdata)
    if not ser.is_valid():
        return Response({'data':ser.errors,"errors":"something went wrong"})
    else:
        ser.save()
        return Response({"data":ser.data,"message":"Employee data update in tables"})
    
@api_view(['DELETE'])   
def delete(request,id):
    sdata = Employee.objects.get(pk=id)
    sdata.delete()
    return Response({"message":'employee delete'})
