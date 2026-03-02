from django.shortcuts import render
from myapp.models import *
from django.http import HttpResponse,JsonResponse


# Create your views here.
def index(request):
    return render(request,"index.html")

def register(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    age = request.POST.get('age')
    dept = request.POST.get('dept')
    salary = request.POST.get('salary')
    date = request.POST.get('date')

    Employee.objects.create(name=name,email=email,age=age,dept=dept,salary=salary,date=date)

    return HttpResponse("Employee Add to table ")

def view(request):
    e = Employee.objects.all()
    return JsonResponse({'e':list(e.values())})


def delete(request):
    eid = request.GET.get('eid')
    e = Employee.objects.get(pk=eid)
    e.delete()
    return HttpResponse("Employee Deteled in recodes ")


def edit(request):
    eid = request.GET.get('eid')
    e = Employee.objects.filter(pk=eid)
    return JsonResponse({'e':list(e.values())})


def update(request):
    if request.method =='POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        dept = request.POST.get('dept')
        salary = request.POST.get('salary')
        date = request.POST.get('date')

        e = Employee.objects.get(pk=id)
        e.name= name
        e.email =email
        e.age =age
        e.dept =dept
        e.salary =salary
        e.date =date
        e.save()

  

    return HttpResponse("Employee update to table ")