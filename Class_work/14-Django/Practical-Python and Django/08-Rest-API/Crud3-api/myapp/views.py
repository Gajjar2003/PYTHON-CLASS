from django.shortcuts import render
from rest_framework.response import Response
from myapp.models import * 
from rest_framework.decorators import api_view
from myapp.serializer import *


@api_view(['GET'])
def view(request):
    techer = Techer.objects.all()
    ser = techerserializer(techer,many=True)
    return Response({'data':ser.data})

@api_view(['POST'])
def add(request):
    sdata = request.data
    ser = techerserializer(data=sdata)
    if not ser.is_valid():
        return Response({'data':ser.errors,"message":'something went wrong'})
    else:
        ser.save()
        return Response({'data':ser.data,'message':'Insert this recode inside a tables'})
    
@api_view(['GET'])
def getbyid(request,id):
    techers = Techer.objects.get(pk=id)
    ser = techerserializer(techers)
    return Response({'data':ser.data})

@api_view(['PUT'])
def edit(request,id):
    sdata = request.data
    cdata = Techer.objects.get(pk=id)
    ser = techerserializer(cdata,sdata)
    if not ser.is_valid():
        return Response({'data':ser.errors,"message":'something went wrong'})
    else:
        ser.save()
        return Response({'data':ser.data,'message':'Update this recode inside a tables'})
    
@api_view(['DELETE'])
def delete(request,id):
    cdata = Techer.objects.get(pk=id)
    cdata.delete()
    return Response({'message':'recods deleted inside a tables'})