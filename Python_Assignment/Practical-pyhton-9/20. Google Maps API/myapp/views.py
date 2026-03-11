from django.shortcuts import render
from myapp.models import *

# Create your views here.
def index(request):
    doctors = Doctor.objects.all()
    return render(request, "index.html", {"doctors": doctors})