from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import razorpay

# Create your views here.
def index(requset):
    return render(requset,"index.html")

def payment(requset):
    amt = requset.GET['amt']
    client = razorpay.Client(auth=("rzp_test_S1Hsg7YN8MlwDU", "ZKs1rK1XnjRDNd4uxjP2NcRJ"))
    data = { "amount": int(amt)*100, "currency": "INR", "receipt": "order_rcptid_11" }
    payment = client.order.create(data=data)
 
    return JsonResponse(payment)