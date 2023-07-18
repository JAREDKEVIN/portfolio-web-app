from django.shortcuts import redirect, render
from django.contrib import messages

# Create your views here.


def home(request):
    return render(request,'home.html')


def about(request):
    return render(request,'about.html')


def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phonenumber=request.POST.get('phonenumber')
        description=request.POST.get('description')
        
        messages.info(request, f'The name is {name} , email is{email} your phone number is  {phonenumber} and the message is: "{description}"')
        
        return redirect('/contact')
        
    return render(request,'contact.html')



def portfolio(request):
    return render(request,'portfolio.html')

def resume(request):
    return render(request,'resume.html')

def services(request):
    return render(request,'services.html')