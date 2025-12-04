from django.shortcuts import render,redirect
from crudapp.models import student

# Create your views here.
def index(requset):
    return  render(requset,"index.html")

def register_student(request):
        id= request.POST.get('id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')


        if not id:
            student.objects.create(name=name,email=email,age=age)
            return render(request, 'index.html',{'success':'student infromation successfully Done'})
        else:
              st = student.objects.get(pk=id)
              st.name = name
              st.email =email
              st.age = age
              st.save()  

              return render(request, 'index.html',{'success':'student Update successfully Done'})


def display(requset):
      
      students = student.objects.all()

      return render(requset,"display.html",{'student' : students})


def delete(requset):
      
      id = requset.GET.get("id")
      st = student.objects.get(id=id)
      st.delete()
      return redirect("display")

def edit(requset):
      
      id = requset.GET.get("id")
      st = student.objects.get(id=id)
      return render(requset,"index.html",{"st" : st})