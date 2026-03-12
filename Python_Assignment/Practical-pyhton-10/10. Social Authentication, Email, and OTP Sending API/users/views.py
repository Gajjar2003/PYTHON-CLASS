from django.http import HttpResponse
import random

def send_otp(request):
    otp = random.randint(1000,9999)
    return HttpResponse(f"OTP sent: {otp}")