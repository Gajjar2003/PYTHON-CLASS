from django.shortcuts import render
from crudapp.models import student

# Create your views here.
def index(requset):
    return  render(requset,"index.html")

def register_student(request):
     
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')

        student.objects.create(name=name,email=email,age=age)

        return render(request, 'index.html',{'success':'student infromation successfully Done'})