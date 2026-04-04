from django.shortcuts import render
from myapp.models import *
from django.http import HttpResponse,JsonResponse


# Create your views here.
def index(request):
    return render(request,"index.html")

def register(request):
    name = request.POST.get('name')
    dept = request.POST.get('dept')
    age = request.POST.get('age')
    salary = request.POST.get('salary')
   

    Employes.objects.create(name=name,dept=dept,age=age,salary=salary)

    return HttpResponse("Employee inserted into Database")

def displayitems(request):
    emp = Employes.objects.all()
    return JsonResponse({'emp':list(emp.values())})

def deleteitems(request):
    eid = request.GET.get('eid')
    emp = Employes.objects.get(pk=eid)
    emp.delete()
    return HttpResponse("Employee delete into tabels")

def edititems(request):
    eid = request.GET.get('eid')
    emp = Employes.objects.filter(pk=eid)
    return JsonResponse({'emp':list(emp.values())})
    

def update(request):
    id = request.POST.get('id')
    name = request.POST.get('name')
    dept = request.POST.get('dept')
    age = request.POST.get('age')
    salary = request.POST.get('salary')
   
    emp = Employes.objects.get(pk=id)
    emp.name=name
    emp.dept = dept
    emp.age = age
    emp.salary=salary
    emp.save()


    return HttpResponse("Employee Update into Database")