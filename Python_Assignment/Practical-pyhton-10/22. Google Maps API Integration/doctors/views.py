from django.shortcuts import render
from .models import Doctor

def map_view(request):
    city = request.GET.get('city')

    if city:
        doctors = Doctor.objects.filter(city__icontains=city)
    else:
        doctors = Doctor.objects.all()

    return render(request, "map.html", {"doctors": doctors})