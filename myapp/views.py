from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def productfn(request):
    # print("hello")
    return render(request, 'product.html')

def billingfn(request):
    # print("hello")
    return render(request, 'billing.html')