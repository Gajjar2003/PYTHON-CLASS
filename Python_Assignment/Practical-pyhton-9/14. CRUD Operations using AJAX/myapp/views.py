from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from myapp.models import *

def index(request):
    return render(request,"index.html")

def register(request):
    name = request.POST.get('name')
    age = request.POST.get('age')
    email = request.POST.get('email')
    dept = request.POST.get('dept')
    salary = request.POST.get('salary')

    Employee.objects.create(name=name,age=age,email=email,dept=dept,salary=salary)
    return HttpResponse("successfully done !!")

def display(request):
    emp = Employee.objects.all()
    return JsonResponse({'emp':list(emp.values())})

def delete(request):
    eid = request.GET.get('eid')
    emp = Employee.objects.get(pk=eid)
    emp.delete()
    return HttpResponse("employee deleted in recods")

def edit(request):
    eid = request.GET.get('eid')
    emp = Employee.objects.filter(pk=eid)
    return JsonResponse({'emp':list(emp.values())})


def update(request):
    id = request.POST.get('id')
    name = request.POST.get('name')
    age = request.POST.get('age')
    email = request.POST.get('email')
    dept = request.POST.get('dept')
    salary = request.POST.get('salary')

    emp  = Employee.objects.get(pk=id)
    emp.name= name
    emp.age =age
    emp.email =email
    emp.dept = dept
    emp.salary =salary
    emp.save()
    return HttpResponse("update employees")
 