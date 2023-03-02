from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Home")

def index(request):
    return HttpResponse("hello world")

def login(request):
    return render(request,'blog/login.html')

def aboutUs(request):
    return render(request,'blog/aboutus.html')

def contactUs(request):

    return render(request,'blog/contactus.html')

def feedback(request):
    
    userName = "parth"
    userEmail = "parth@gmail.com"
    context ={
        'userName':userName,
        'userEmail':userEmail,
    }
    
    
    return render(request,'blog/feedback.html',context)

