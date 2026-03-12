from django.shortcuts import render
import requests

def country_info(request):

    data = None

    if request.method == "POST":
        country = request.POST.get("country")

        url = f"https://restcountries.com/v3.1/name/{country}"

        response = requests.get(url)
        res = response.json()

        if isinstance(res, list):

            population = res[0]["population"]

            languages = list(res[0]["languages"].values())

            currency = list(res[0]["currencies"].keys())[0]

            data = {
                "country": country,
                "population": population,
                "languages": languages,
                "currency": currency
            }

    return render(request,"country.html",{"data":data})