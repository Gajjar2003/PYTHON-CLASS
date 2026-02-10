from django.shortcuts import render
from myapp.models import *

# Create your views here.

def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        pro = Product.objects.create(name=name)

        images = request.FILES.getlist("image")
        for img in images:
            Image.objects.create(product=pro, image=img)

    product = Product.objects.all()
    return render(request, "index.html", {"product": product})
