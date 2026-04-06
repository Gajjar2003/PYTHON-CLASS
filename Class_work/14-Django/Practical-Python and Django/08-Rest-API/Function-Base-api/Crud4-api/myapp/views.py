from django.shortcuts import render
from rest_framework.response import Response
from myapp.models import *
from myapp.serailzer import *
from rest_framework.decorators import api_view

@api_view(['GET'])
def view(request):
    mo = Moblie.objects.all()
    ser = moblieserlizer(mo,many=True)
    return Response({'data':ser.data})

@api_view(['POST'])
def add(request):
    ser = moblieserlizer(data=request.data)
    if not ser.is_valid():
        return Response({'errors':ser.errors,"megsses":'something went wrogn'})
    else:
        ser.save()
        return Response({"data":ser.data,"message":"MOblie data inserted in tbales"})
    
@api_view(['GET'])
def getbyid(request,id):
    mo = Moblie.objects.get(pk=id)
    ser = moblieserlizer(mo)
    return Response({'data':ser.data})

@api_view(['PUT'])
def edit(request,id):
    data = request.data
    cdata = Moblie.objects.get(pk=id)
    ser = moblieserlizer(cdata,data)
    if not ser.is_valid():
        return Response({'errors':ser.errors,"megsses":'something went wrogn'})
    else:
        ser.save()
        return Response({"data":ser.data,"message":"MOblie data Update in tbales"})
  
@api_view(['delete'])
def delete(request,id):
    sdata =Moblie.objects.get(pk=id)
    sdata.delete()
    return Response({"message":"moblie data Deleted in tables"})
