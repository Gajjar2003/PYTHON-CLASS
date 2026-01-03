from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .models import student
from django.db.models import Q


def index(request):
    return render(request, "index.html")


def register(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")

        student.objects.create( name=name,email=email,phone=phone)

    return JsonResponse("Student Added Successfully", safe=False)



def display(request):
    students = student.objects.all()
    return JsonResponse({"students":list(students.values())})

def delete(request):
    sid = request.GET['sid']
    st = student.objects.get(pk=sid)
    st.delete()
    return HttpResponse("Student Deleted")

def getbyid(request):
    sid = request.GET['sid']
    st = student.objects.filter(id=sid)
    return JsonResponse({"student":list(st.values())})

def update(requset):
     if requset.method == "POST":
        id = requset.POST.get('id')
        name = requset.POST.get("name")
        email = requset.POST.get("email")
        phone = requset.POST.get("phone")

        s = student.objects.get(pk=id)
        s.name =name
        s.email =email
        s.phone =phone
        s.save()
     
        return JsonResponse("Update Successfully", safe=False)
     
def search(request):
    value = request.GET['value']
    students = student.objects.filter(Q(name__startswith=value)|Q(email__startswith=value)|Q(phone__startswith=value)) 
    return JsonResponse({"students":list(students.values())})
