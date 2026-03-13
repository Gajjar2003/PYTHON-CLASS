from django.shortcuts import render
from .forms import RegisterForm
from .otp_service import send_otp

def register(request):

    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']

            otp = send_otp(phone)

            request.session['otp'] = otp
            request.session['phone'] = phone

            return render(request,"verify.html")

    return render(request,"register.html",{"form":form})


def verify_otp(request):

    if request.method == "POST":
        user_otp = request.POST.get("otp")
        session_otp = request.session.get("otp")

        if str(user_otp) == str(session_otp):
            return render(request,"success.html")
        else:
            return render(request,"verify.html",{"error":"Invalid OTP"})