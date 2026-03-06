from django.shortcuts import render
from rest_framework.response import Response
from myapp.models import *
from myapp.serializer import *
from rest_framework.decorators import api_view


@api_view(['GET'])
def view(request):
    product =Product.objects.all()
    ser = productserializer(product,many=True)
    return Response(ser.data)

@api_view(['POST'])
def add(request):
    sdata = request.data
    ser = productserializer(data=sdata)
    if not ser.is_valid():
        return Response({'data':ser.errors,'message' :'something went wrong'})
    else:
        ser.save()
        return Response({'data':ser.data,'message':'Products inserted in recods'})
    
@api_view(['GET'])
def getbyid(request,id):
    products = Product.objects.get(pk=id)
    ser = productserializer(products)
    return Response({"data":ser.data})


@api_view(['DELETE'])
def delete(request,id):
    products = Product.objects.get(pk=id)
    products.delete()
    return Response({'message':'products deleted in recods '})


@api_view(['PUT'])
def edit(request,id):
    sdata = request.data
    cdata = Product.objects.get(pk=id)
    ser =productserializer(cdata,sdata)
    if not ser.is_valid():
        return Response({'data':ser.errors,'message' :'something went wrong'})
    else:
        ser.save()
        return Response({'data':ser.data,'message':'Products updated in recods'})


