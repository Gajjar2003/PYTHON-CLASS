from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from myapp.models import *

# Create your views here.
def index(request):
    return render(request,"index.html")

def register(request):
    if request.method == "POST":

        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        marks = request.POST.get('marks')
        subject = request.POST.get('subject')

        Student.objects.create( name=name,email=email,age=age,marks=marks,subject=subject )

        return HttpResponse("Student add into records !!")
    

def display(request):
    st = Student.objects.all()
    return JsonResponse({'st':list(st.values())})

def delete(request):
    sid = request.GET.get('sid')
    st = Student.objects.get(pk=sid)
    st.delete()
    return HttpResponse("Student remove in tables")

def edit(request):
    sid = request.GET.get('sid')
    st = Student.objects.filter(pk=sid)
    return JsonResponse({'st':list(st.values())})

def update(request):
        id  =  request.POST.get('id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        marks = request.POST.get('marks')
        subject = request.POST.get('subject')

        st = Student.objects.get(pk=id)
        st.name = name
        st.email = email
        st.age = age
        st.marks = marks
        st.subject=subject
        st.save()
        return HttpResponse("Update student in recods")