from django.shortcuts import render
from myapp.models import *

def index(request):
    students = Student.objects.all()
    return render(request,"index.html",{'students':students})
