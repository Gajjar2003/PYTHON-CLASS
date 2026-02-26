from django.shortcuts import render
from myapp.models import *
from django.http import HttpResponse,JsonResponse

# Create your views here.
def index(request):
    return render(request,"index.html")

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')

    Student.objects.create(name=name,email=email,age=age)
    return HttpResponse("register successfully done")

def display(request):
    st = Student.objects.all()
    return JsonResponse({'st':list(st.values())})

def delete(request):
    sid = request.GET.get('sid')
    s = Student.objects.get(pk=sid)
    s.delete()
    return HttpResponse("Student delete")
    
def edit(request):
    sid = request.GET.get('sid')
    st = Student.objects.filter(id=sid)
    return JsonResponse({'st':list(st.values())})

def update(request):
     if request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')

        st = Student.objects.get(pk=id)
        st.name =name
        st.email =email
        st.age =age
        st.save()
        return HttpResponse("Update successfully done")