from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,APIView
from myapp.models import *
from myapp.serializer import *

class Subjectapi(APIView):

    def get(self,request):
        st = Subject.objects.all()
        ser = Subjectserializer(st,many=True)
        return Response({'data':ser.data})
    
    def post(self,request):
        ser = Subjectserializer(data = request.data)
        if not ser.is_valid():
            return Response({'data':ser.errors,'errors':"something went wrong"})
        else:
            ser.save()
            return Response({'data':ser.data,'message' : "Data inside a recods"})
        
class Subjectidapi(APIView):

    def get(self,request,id):
        st = Subject.objects.get(pk=id)
        ser = Subjectserializer(st)
        return Response({'data':ser.data})
    
    def put(self,request,id):
        st = Subject.objects.get(pk=id)
        ser = Subjectserializer(st,request.data)
        if not ser.is_valid():
            return Response({'data':ser.errors})
        else:
            ser.save()
            return Response({'data':ser.data})
        
    def delete(self,request,id):
        st = Subject.objects.get(pk=id)
        st.delete()
        return Response({'message':'data delete inside a recods'})

@api_view(['POST'])
def viewstudent(request, id):
    ser = Studentserializer(data=request.data)
    if ser.is_valid():
        ser.save(subject_id=id)
        return Response({'data': ser.data})
    return Response({'error': ser.errors})

@api_view(['GET'])
def studentview(request):
    st = Student.objects.all()
    ser = Studentserializer(st,many=True)
    return Response({'data':ser.data})
