from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from myapp.models import Doctor
from myapp.serializer import *


class DoctorPagination(PageNumberPagination):
    page_size = 3   

class DoctorListAPI(ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = Doctorserializer
    pagination_class = DoctorPagination