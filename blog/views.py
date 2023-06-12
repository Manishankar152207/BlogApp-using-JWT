from django.shortcuts import render
from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def myblog(request):
    return render(request, 'index.html')

def addblog(request):
    return render(request, 'addblog.html')

def blogdetail(request):
    return render(request, 'blogdetail.html')