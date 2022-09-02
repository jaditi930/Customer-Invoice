from cgi import print_exception
from http.client import HTTPResponse
import json
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
        print(type(request.POST))
        name=request.POST["name"]
        emailad=request.POST["email"]
        phone=request.POST["phone"]
        itemname=json.dumps(request.POST.getlist('itemname'))
        quant=json.dumps(request.POST.getlist("quantity"))
        pric=json.dumps(request.POST.getlist('price'))
        category=json.dumps(request.POST.getlist("category"))
        print(type(pric))
        InvoiceForm.objects.create(name=name,email=emailad,phone=phone,itemname=itemname,quantity=quant,price=pric,category=category)
        return redirect("/show_all/")
    return redirect("/")

def show_all(request):
    cust_info=InvoiceForm.objects.all()
    inames=InvoiceForm.objects.values('itemname')
    list_names=list()
    for i in range(inames.count()):
      list_names.append(inames[i]['itemname'])
    for i in range (inames.count()):
        try:
            list_names[i]=json.loads(list_names[i])
        except json.decoder.JSONDecodeError:
            pass
    print(list_names)
    names_dict=list()
    for i,j in zip(list_names,cust_info):
        dic=dict()
        dic["itemname"]=i
        dic["name"]=j.name
        dic["email"]=j.email
        dic["phone"]=j.phone
        names_dict.append(dic)
    print(names_dict)
    context={"cust_info":cust_info,"names":names_dict}
    return render(request,"show_invoices.html",context)

