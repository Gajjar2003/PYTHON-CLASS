from django.shortcuts import render
from myapp.models import *


def index(request):
    doctors =Decotor.objects.all()
    return render(request,"index.html",{'doctors':doctors})


