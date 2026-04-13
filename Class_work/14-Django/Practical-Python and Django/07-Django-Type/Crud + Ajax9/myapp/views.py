from django.shortcuts import render
from myapp.models import *
from django.http import HttpResponse,JsonResponse



def index(request):
    return render(request,"index.html")

def register(request):
    name = request.POST.get('name')
    age = request.POST.get('age')
    phone = request.POST.get('phone')
    subject = request.POST.get('subject')

    Jenil.objects.create(name=name,age=age,phone=phone,subject=subject)
    return HttpResponse("Add into tables")

def display(request):
    st = Jenil.objects.all()
    return JsonResponse({'st':list(st.values())})

def delete(request):
    sid = request.GET.get('sid')
    st = Jenil.objects.get(pk=sid)
    st.delete()
    return HttpResponse("Delete items")

def edit(request):
    sid = request.GET.get('sid')
    st = Jenil.objects.filter(pk=sid)
    return JsonResponse({'st':list(st.values())})

def update(request):
    id = request.POST.get('id')
    name = request.POST.get('name')
    age = request.POST.get('age')
    phone = request.POST.get('phone')
    subject = request.POST.get('subject')

    st= Jenil.objects.get(pk=id)
    st.name=name
    st.age=age
    st.subject = subject
    st.phone = phone
    st.save()

    return HttpResponse("Update into tables")
