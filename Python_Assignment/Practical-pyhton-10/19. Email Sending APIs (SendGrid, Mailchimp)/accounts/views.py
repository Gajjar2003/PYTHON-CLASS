from django.shortcuts import render
from .forms import RegisterForm
from .email_service import send_confirmation_email

def register(request):

    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            # Send confirmation email
            send_confirmation_email(email, name)

            return render(request,"success.html")

    return render(request,"register.html",{"form":form})