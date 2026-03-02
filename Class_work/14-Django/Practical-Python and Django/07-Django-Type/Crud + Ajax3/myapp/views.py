from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from myapp.models import * 

# Create your views here.
def index(request):
    return render(request,"index.html")

def register(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    subject =request.POST.get('subject')
    age = request.POST.get('age')
    marks = request.POST.get('marks')

    Student.objects.create(name=name,email=email,subject=subject,age=age,marks=marks)
    return HttpResponse("Student recode successfully done !!")


def view(request):
   student = Student.objects.all()
   return JsonResponse({'student':list(student.values())})

def delete(request):
    sid = request.GET.get('sid')
    st = Student.objects.get(pk=sid)
    st.delete()
    return HttpResponse('Student recode deleted in tables')

def getbyid(request):
    sid = request.GET.get('sid')
    s = Student.objects.filter(pk=sid)
    return JsonResponse({'s':list(s.values())})

def update(request):
    if request.method == "POST":
        id = request.POST.get("id")
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        age = request.POST.get("age")
        marks = request.POST.get("marks")

        s = Student.objects.get(pk=id)
        s.name = name
        s.email = email
        s.subject = subject
        s.age = age
        s.marks = marks
        s.save()

        return HttpResponse("Student record updated successfully")