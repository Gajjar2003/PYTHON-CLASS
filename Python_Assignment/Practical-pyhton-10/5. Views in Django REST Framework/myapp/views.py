from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,APIView
from myapp.models import *
from myapp.serializer import *


class doctorapi(APIView):

    def get(self,request):
        doctors = Doctors.objects.all()
        ser = Doctorserializer(doctors ,many=True)
        return Response({'data':ser.data})
    
    def post(self,request):
        
        ser = Doctorserializer(data = request.data)
        if not ser.is_valid():
            return Response({'error':ser.errors})
        else:
            ser.save()
            return Response({'data':ser.data})
        
class doctoridapi(APIView):

    def get(self,request,id):
        doc = Doctors.objects.get(pk=id)
        ser = Doctorserializer(doc)
        return Response({'data':ser.data})
    
    def put(self,request,id):
        doc = Doctors.objects.get(pk=id)
        ser = Doctorserializer(doc,request.data)
        if not ser.is_valid():
            return Response({'error':ser.errors})
        else:
            ser.save()
            return Response({'data':ser.data})
        

    def delete(self,request,id):
         doc = Doctors.objects.get(pk=id)
         doc.delete()
         return Response({'meg':'deleted'})




