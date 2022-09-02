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
    inames=InvoiceForm.objects.values('id','name','email','phone')
    
    context={"names":inames}
    return render(request,"show_invoices.html",context)

def generate(request,id):
    obj=InvoiceForm.objects.get(id=id)
    try:
      names=json.loads(obj.itemname)
      prices=json.loads(obj.price)
      category=json.loads(obj.category)
      quantity=json.loads(obj.quantity)
      itemlist=list()
      for i,j,k,l in zip(names,prices,quantity,category):
            itemdict=dict()
            itemdict["name"]=i
            itemdict["price"]=j
            itemdict["quantity"]=k
            itemdict["category"]=l
            itemlist.append(itemdict)
            print(itemlist)
      return render(request,"generateInvoice.html",{"obj":obj,"items":itemlist})
    except json.decoder.JSONDecodeError:
        names=obj.itemname
        prices=obj.price
        category=obj.category
        quantity=obj.quantity
        itemlist=list()
        itemdict={"name":names,"price":prices,"quantity":quantity,"category":category}
        itemlist.append(itemdict)
        print(itemlist)
        return render(request,"generateInvoice.html",{"obj":obj,"items":itemlist})


