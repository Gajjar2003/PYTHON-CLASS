from rest_framework.decorators import api_view
from rest_framework.response import Response
from myapp.models import *
from myapp.serializer import * 


@api_view(['GET'])
def doctor_list(request):
    doctors = Doctor.objects.all()
    serializer = DoctorSerializer(doctors, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add(request):
    ser = DoctorSerializer(data=request.data)
    if not ser.is_valid():
        return Response({'data':ser.errors})
    else:
        ser.save()
        return Response({'data':ser.data})