from django.shortcuts import render
import requests

TOKEN = "YOUR_GITHUB_TOKEN"
USERNAME = "Gajjar2003"


def list_repos(request):

    url = f"https://api.github.com/users/{USERNAME}/repos"

    response = requests.get(url)
    repos = response.json()

    repo_names = []

    if isinstance(repos, list):
        for repo in repos:
            repo_names.append(repo["name"])

    return render(request,"repos.html",{"repos":repo_names})


def create_repo(request):

    url = "https://api.github.com/user/repos"

    headers = {
        "Authorization": f"token {TOKEN}"
    }

    data = {
        "name": "django-api-repo",
        "private": False
    }

    response = requests.post(url,json=data,headers=headers)

    return render(request,"create.html",{"response":response.json()})