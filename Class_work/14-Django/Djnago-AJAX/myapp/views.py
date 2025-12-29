from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import *
from django.http import JsonResponse

# Create your views here.
def index(requset):
    return render(requset,"index.html")

# def view(requset):
#     data = requset.GET['data']
#     row = ""
#     if data == 'sporst':
#         row+= "<ul><li>Ball</li><li>Bat</li><li>Stmup</li></ul>"
#     elif data == "electric":
#         row+= "<ul><li>Tv</li><li>Pc</li><li>Laptop</li></ul>"
#     else:
#         row+="Not data found"

#     return HttpResponse(row)

def view(request):
    data = request.GET['data']
    products = product.objects.filter(name__startswith=data)
    return JsonResponse({"products":list(products.values())})

def countries(request):
    countries = Country.objects.all()
    return JsonResponse({"countries":list(countries.values())})

def states(request):
    cid = request.GET['cid']
    states = State.objects.filter(country_id=cid)
    return JsonResponse({"states":list(states.values())})

def cities(request):
    sid = request.GET['sid']
    cities = City.objects.filter(state_id=sid)
    return JsonResponse({"cities":list(cities.values())})
