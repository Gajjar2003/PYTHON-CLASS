from django.shortcuts import render
import requests

def location(request):

    address = "Surat Gujarat"
    api_key = "YOUR_GOOGLE_API_KEY"

    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}"

    response = requests.get(url)
    data = response.json()

    if data["status"] == "OK":

        latitude = data["results"][0]["geometry"]["location"]["lat"]
        longitude = data["results"][0]["geometry"]["location"]["lng"]

        location_data = {
            "address": address,
            "latitude": latitude,
            "longitude": longitude
        }

    else:
        location_data = {
            "address": address,
            "latitude": "Not Found",
            "longitude": "Not Found"
        }

    return render(request,"location.html",{"location":location_data})