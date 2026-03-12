from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response
from myapp.models import *
from myapp.serializer import *


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view(request):
    jenil = Jenil.objects.all()
    serializer = Jenilserilizer(jenil, many=True)

    return Response(serializer.data)

@api_view(['POST'])
def add(request):
    ser = Jenilserilizer(data = request.data)
    if not ser.is_valid():
        return Response({'errors':ser.errors})
    else:
        ser.save()
        return Response({'data':ser.data})
    
@api_view(['GET'])
def get(request,id):
    jenil = Jenil.objects.get(pk=id)
    ser = Jenilserilizer(jenil)
    return Response({"data":ser.data})

@api_view(['PUT'])
def put(request,id):
    jenil = Jenil.objects.get(pk=id)
    ser = Jenilserilizer(jenil,request.data)
    if not ser.is_valid():
        return Response({'errors':ser.errors})
    else:
        ser.save()
        return Response({'data':ser.data})
    
@api_view(['DELETE'])
def delete(request,id):
    jenil = Jenil.objects.get(pk=id)
    jenil.delete()
    return Response({'meg':"all data deleted in recods "}) 