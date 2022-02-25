from django.http import Http404
from django.shortcuts import redirect, render
from django.shortcuts import HttpResponse
from Shortner.models import urlModel
import random
# Create your views here.

def home(request):
    return render(request,"landingpage.html")

def makeshorturl(request):
    if request.method == "POST":
        longurl = request.POST['longurl']
        s="abcdefghijklmnoparstuvcyzABCDEFGHIJKLMNOPORSTUMKYZ1234567890!@#$%*"
        shorturl=("".join(random.sample(s,7)))
        obj = urlModel.objects.create(longurl = longurl,shorturl = shorturl)
        print("object created")
        shorturl = "http://127.0.0.1:8000/"+shorturl

    #return HttpResponse("Your shorturl for {} is {}".format(longurl,shorturl))
    return render(request,"result.html",context={"shorturl":shorturl,"longurl":longurl})

def redirecturl(request,shorturl):
    print (shorturl)
    try:
       obj = urlModel.objects.get(shorturl=shorturl)
    except urlModel.DoesNotExist:
        obj = None
 

    if obj !=None:
        print("object found")
        print(obj.longurl)
        obj.count+=1
        obj.save()
        return redirect(obj.longurl)
    else:
        return HttpResponse("check your url")
        