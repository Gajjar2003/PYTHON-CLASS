from django.shortcuts import render


# Create your views here.

def index(request):
        return render(request,"index.html")

def about(request):
        return render(request,"about.html")
   
def phone(request):
        return render(request,"phone.html")

def help(requset):
        return render(requset,"help.html")