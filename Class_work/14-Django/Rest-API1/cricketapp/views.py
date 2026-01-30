from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,APIView,permission_classes
from cricketapp.models import *
from cricketapp.serializer import *
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly
class cricketAPI(APIView):

    def get(self, request):
        depts = CricketDept.objects.all()
        ser = cricketdeptserializer(depts, many=True)
        return Response({'data': ser.data})

    def post(self, request):
        ser = cricketdeptserializer(data=request.data)
        if not ser.is_valid():
            return Response({'errors': ser.errors})
        ser.save()
        return Response({'data': ser.data})
    

class  cricketbyid(APIView):

    def get(self,requset,id):
        dept = CricketDept.objects.get(pk=id)
        ser = cricketdeptserializer(dept)
        return Response({'data': ser.data})
    

    def delete(self,requset,id):
        dept = CricketDept.objects.get(pk=id)
        dept.delete()
        return Response({'meg':'Data Delete'})
    
    def put(self,request,id):
        dept = CricketDept.objects.get(pk=id)
        ser = cricketdeptserializer(dept, data=request.data)
        if not ser.is_valid():
            return Response({'errors': ser.errors})
        ser.save()
        return Response({'data': ser.data})
    

@api_view(['POST'])
def addcricket(request,id)  :
    data = request.data
    data.update({"dept":id})
    ser = cricketserializer(data=data)
    if not ser.is_valid():
        return Response({"errors":ser.errors})
    else:
        ser.save()
        return Response({"data":ser.data})
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getcricket(request):
 
    cri = Cricketdetalis.objects.all()
    serializer = cricketserializer(cri, many=True)
    return Response({"data": serializer.data})

@api_view(['PUT'])
def updatecricket(requset,id,cid):
    data = requset.data
    data.update({"dept":id})
    cdata = Cricketdetalis.objects.get(pk=cid)
    ser = cricketserializer(cdata,data)
    if not ser.is_valid():
        return Response({"errors":ser.errors})
    else:
        ser.save()
        return Response({"data":ser.data})
  

class cricketbyid(APIView):
    
       def get(self, request, id):
        cri = Cricketdetalis.objects.get(pk=id)
        ser = cricketserializer(cri)
        return Response({'data': ser.data})
       

       def delete(self,requset,id):
           cri = Cricketdetalis.objects.get(pk=id)
           cri.delete()
           return Response({'meg':'data deleted'})
       

      
           
        
    

