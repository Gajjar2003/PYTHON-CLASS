from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from crudapp.models import *
from crudapp.serializer import *

@api_view(['GET'])
def view_student(requset):
    s = student.objects.all()
    ser = studentserializer(s,many=True)
    return Response({'data':ser.data})

@api_view(['POST'])
def add_student(requset):
    stdata = requset.data
    ser = studentserializer(data = stdata)
    if not ser.is_valid():
        return Response({"errors":ser.errors,"Message":'something went wrong'})
    else:
        ser.save()
        return Response({"data":ser.data,'message':' data inersted successfully done !'})

@api_view(['GET'])    
def view_byid(requset,id):
    s = student.objects.get(pk=id)
    ser = studentserializer(s)
    return Response({"data":ser.data})

@api_view(['PUT'])
def edit_student(requset,id):
    sdata = requset.data
    cdata = student.objects.get(pk=id)
    ser = studentserializer(cdata,sdata)
    if not ser.is_valid():
        return Response({"errors":ser.errors,"Message":'something went wrong'})
    else:
        ser.save()
        return Response({"data":ser.data,'message':' data Edit successfully done !'})
    
@api_view(['DELETE'])    
def delete_student(requset,id):
    sdata = student.objects.get(pk=id)
    sdata.delete()
    return Response({"message":'data deleted'})
   


  