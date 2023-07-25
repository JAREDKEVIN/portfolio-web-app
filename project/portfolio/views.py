from django.shortcuts import redirect, render
from django.contrib import messages
from portfolio.models import Contact

# Create your views here.


def home(request):
    return render(request,'home.html')


def about(request):
    return render(request,'about.html')


def contact(request):
    if request.method=="POST":
        fname=request.POST.get('name')
        femail=request.POST.get('email')
        fphonenumber=request.POST.get('phonenumber')
        fdescription=request.POST.get('description')
        query=Contact(name=fname,email=femail,phonenumber=fphonenumber,description=fdescription)
        query.save()
        messages.success(request,"Thanks for contacting,We will get back to you soonest!!")
        # messages.info(request, f'The name is {name} , & email is {email} your phone number is {phonenumber} and the message is: "{description}"')
        
        return redirect('/contact')
    
    return render(request,'contact.html')



def portfolio(request):
    return render(request,'portfolio.html')

def resume(request):
    return render(request,'resume.html')

def services(request):
    return render(request,'services.html')