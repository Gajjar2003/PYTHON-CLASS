from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import razorpay
from django.core.mail import send_mail
from django.conf import settings


def index(requset):
    return render(requset,"index.html")

def payment(requset):
    amt = requset.GET['amt']
    client = razorpay.Client(auth=("rzp_test_S1Hsg7YN8MlwDU", "ZKs1rK1XnjRDNd4uxjP2NcRJ"))
    data = { "amount": int(amt)*100, "currency": "INR", "receipt": "order_rcptid_11" }
    payment = client.order.create(data=data)
 
    return JsonResponse(payment)

def sendmail(requset):
    context = {}
    if requset.method == 'POST':
        address = requset.POST.get('address')
        subject = requset.POST.get('subject')
        message = requset.POST.get('message')

        if address and subject and message:
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, [address])
                context['result'] = 'Email sent successfully'
            except Exception as e:
                context['result'] = f'Error sending email: {e}'
        else:
            context['result'] = 'All fields are required'
    
    return render(requset,"mail.html",context)
   