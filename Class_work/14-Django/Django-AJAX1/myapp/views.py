from django.shortcuts import render
from myapp.models import *
from django.http import JsonResponse,HttpResponse

# Create your views here.
def index(requset):
    return render(requset,"index.html")

def register(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")

        student.objects.create(name=name,email=email,phone=phone)

        return HttpResponse("Register successfully done !")
    
def display(requset):
    students = student.objects.all()
    return JsonResponse({"students":list(students.values())})