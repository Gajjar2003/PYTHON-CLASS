from django.shortcuts import render
from myapp.models import *
from django.http import HttpResponse,JsonResponse

# Create your views here.
def index(request):
    return render(request,"index.html")

def register(request):
   name = request.POST.get('name')
   age = request.POST.get('age')
   email = request.POST.get('email')
   phone = request.POST.get('phone')
   subject  = request.POST.get('subject')
   Student.objects.create(name=name,age=age,email=email,phone=phone,subject=subject)
   return HttpResponse("Student Inside a Tables")

def display(request):
    st = Student.objects.all()
    return JsonResponse({'st':list(st.values())})

def delete(request):
    sid = request.GET.get('sid')
    st = Student.objects.get(pk=sid)
    st.delete()
    return HttpResponse("Student Delete inside a Tables")

def edit(request):
    sid = request.GET.get('sid')
    st = Student.objects.filter(pk=sid)
    return JsonResponse({'st':list(st.values())})

def update(request):
    id = request.POST.get('id')
    name = request.POST.get('name')
    age = request.POST.get('age')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    subject  = request.POST.get('subject')

    st = Student.objects.get(pk=id)
    st.name=name
    st.age = age
    st.email =email
    st.phone = phone
    st.subject =subject
    st.save()
    
    return HttpResponse("Student Update Inside a Tables")
