from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,APIView
from company.models import *
from company.serializer import *


class Deptapi(APIView):

    def get(self,request):
        dept = Dept.objects.all()
        ser = Deptserializer(dept,many=True)
        return Response({'data':ser.data})
    
    def post(self,request):
        ser = Deptserializer(data = request.data)
        if not ser.is_valid():
            return Response({'data':ser.errors})
        else:
            ser.save()
            return Response({"data":ser.data})
        
class Deptbyid(APIView):

    def get(self,request,id):
        dept = Dept.objects.get(pk=id)
        ser = Deptserializer(dept)
        return Response({'data':ser.data})
    

    def delete(self,request,id):
        dept = Dept.objects.get(pk=id)
        dept.delete()
        return Response({'message':'dept delete'})
    
    def put(self,request,id):
        dept = Dept.objects.get(pk=id)
        ser =Deptserializer(dept,request.data)
        if not ser.is_valid():
            return Response({'data':ser.errors})
        else:
            ser.save()
            return Response({"data":ser.data})
    
@api_view(['POST'])
def addemp(request,id):
    data = request.data
    data.update({'dept':id})
    ser = Empserializer(data=data)
    if not ser.is_valid():
        return Response({'data':ser.errors})
    else:
        ser.save()
        return Response({"data":ser.data})


@api_view(['GET'])
def emps(request):
    emps = Emp.objects.all()
    ser = Empserializer(emps,many=True)
    return Response({'data':ser.data})


@api_view(['DELETE'])
def delete(request,id):
    emps = Emp.objects.get(pk=id)
    emps.delete()
    return Response({'message':"delete"})


