from django.shortcuts import render
from rest_framework.response import Response
from myapp.models import *
from rest_framework.decorators import api_view
from myapp.serializer import *

@api_view(['GET'])
def view(request):
    student = Student.objects.all()
    ser = Studentserializer(student,many=True)
    return Response(ser.data)


@api_view(['POST'])
def add(request):
    data = request.data
    ser =Studentserializer(data=data)
    if not ser.is_valid():
        return Response({'errors':ser.errors,"megsses":'something went wrogn'})
    else:
        ser.save()
        return Response({"data":ser.data,"message":"Student data inserted in tbales"})
    


@api_view(['GET'])
def getbyid(request,id):
    student =Student.objects.get(pk=id)
    ser = Studentserializer(student)
    return Response({'data':ser.data})
    


@api_view(['PUT'])
def put(request,id):
    data = request.data
    cdata = Student.objects.get(pk=id)
    ser =Studentserializer(cdata,data)
    if not ser.is_valid():
        return Response({'errors':ser.errors,"megsses":'something went wrogn'})
    else:
        ser.save()
        return Response({"data":ser.data,"message":"Student data inserted in tbales"})
    
           
@api_view(['delete'])
def delete(request,id):
    sdata =Student.objects.get(pk=id)
    sdata.delete()
    return Response({"message":"Student data Deleted in tables"})

