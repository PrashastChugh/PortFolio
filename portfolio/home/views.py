from django.shortcuts import render, HttpResponse
from home import models                         #added
# Create your views here.
def home(request):
    #return HttpResponse("This is my home page")
    context = {'name':'Donnie','course':'Django'}
    return render(request,'home.html',context)

def about(request):
    #return HttpResponse("This is my about page")
    return render(request,'about.html')

def project(request):
    #return HttpResponse("This is my project page")
    return render(request,'project.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        print(name, email, phone, desc)

        contact = models.Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        print("The data has been written to the db")


    #return HttpResponse("This is my contact page")
    return render(request,'contact.html')