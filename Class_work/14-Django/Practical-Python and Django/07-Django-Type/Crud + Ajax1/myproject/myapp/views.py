from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from myapp .models import *

def index(request):
    return render(request,"index.html")

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        dept = request.POST.get('dept')
        salary = request.POST.get('salary')

        Employee.objects.create(name=name,email=email,age=age,dept=dept,salary=salary)
        return HttpResponse("Register successfully done !!")
    

def display(request):
    e = Employee.objects.all()
    return JsonResponse({'e':list(e.values())})

def delete(request):
 eid = request.GET.get('eid')
 e = Employee.objects.get(id=eid)
 e.delete()
 return HttpResponse("Employee deleted in recods")

def edit(request):
    eid = request.GET.get('eid')
    e = Employee.objects.filter(pk=eid)
    return JsonResponse({'e':list(e.values())})

def update(request):
     if request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        dept = request.POST.get('dept')
        salary = request.POST.get('salary')

        e =Employee.objects.get(pk=id)
        e.name =name
        e.email =email
        e.age = age
        e.dept =dept
        e.salary =salary
        e.save()

      
        return HttpResponse("Update successfully done !!")
  

