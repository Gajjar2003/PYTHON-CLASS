from django.shortcuts import render
import requests

BEARER_TOKEN = "YOUR_TWITTER_BEARER_TOKEN"
USER_ID = "USER_ID"

def latest_tweets(request):

    url = f"https://api.twitter.com/2/users/{USER_ID}/tweets"

    headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}"
    }

    params = {
        "max_results": 5
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    tweets = []

    if "data" in data:
        for tweet in data["data"]:
            tweets.append(tweet["text"])

    return render(request,"tweets.html",{"tweets":tweets})