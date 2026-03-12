from django.shortcuts import render
import requests

def weather(request):

    city = "Surat"
    api_key = "YOUR_API_KEY"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()

    if "main" in data:
        weather_data = {
            "city": city,
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"]
        }
    else:
        weather_data = {
            "city": city,
            "temperature": "Not available",
            "description": data.get("message","Error fetching weather")
        }

    return render(request,"weather.html",{"weather":weather_data})