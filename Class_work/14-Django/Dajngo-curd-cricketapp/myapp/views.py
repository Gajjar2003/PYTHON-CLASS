from django.shortcuts import render, redirect
from myapp.models import cricket

def index(request):
    return render(request, "index.html")


def register(request):
    if request.method == "POST":

        id = request.POST.get('id')   
        no = request.POST.get('no')
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        type = request.POST.get('type')
        fromate = request.POST.get('fromate')
        run = request.POST.get('run')
        con = request.POST.get('con')
        score = request.POST.get('score')
        avg = request.POST.get('avg')
        four = request.POST.get('four')
        six = request.POST.get('six')

    
        if id == "" or id is None:
            cricket.objects.create(
                no=no,
                name=name,
                age=age,
                email=email,
                type=type,
                fromate=fromate,
                run=run,
                con=con,
                score=score,
                avg=avg,
                four=four,
                six=six
            )
            return render(request,"index.html",{'meg':'successfull Done !'})

  
        else:
            c = cricket.objects.get(id=id)
            c.no = no
            c.name = name
            c.age = age
            c.email = email
            c.type = type
            c.fromate = fromate
            c.run = run
            c.con = con
            c.score = score
            c.avg = avg
            c.four = four
            c.six = six
            c.save()   

            return render(request,"index.html",{'meg':'successfull upadte Done !'})



def display(requset):

    crickets = cricket.objects.all()

    return render(requset,"display.html",{'crickets':crickets})

def delete(requset):
    id = requset.GET.get('id')
    c = cricket.objects.get(id=id)
    c.delete()
    return redirect("display")

def edit(requset):
    id = requset.GET.get('id')
    c = cricket.objects.get(id=id)
    return render(requset,"index.html",{'c':c})