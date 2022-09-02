from cgi import print_exception
from http.client import HTTPResponse
from django.http import HttpResponseRedirect
from statistics import quantiles
from unicodedata import name
from django.shortcuts import render,redirect
from .models import InvoiceForm
# Create your views here.
def index(request):
    return render(request,'index.html')


def succeed(request):
    if request.method=="POST":
        print(request.POST)
        name=request.POST["name"]
        emailad=request.POST["email"]
        phone=request.POST["phone"]
        itemname=request.POST["itemname"]
        quant=request.POST["quantity"]
        pric=request.POST["price"]
        category=request.POST["category"]
        InvoiceForm.objects.create(name=name,email=emailad,phone=phone,itemname=itemname,quantity=quant,price=pric,category=category)
        return redirect("/show_all/")
    return render(request,"index.html")



def show_all(request):
    invoice_list=InvoiceForm.objects.all()
    context={"invoice_list":invoice_list}
    return render(request,"show_invoices.html",context)

