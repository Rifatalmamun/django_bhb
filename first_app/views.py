from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# here is my first django comment

def welcome(request):
    return HttpResponse("<h3>Welcome Django</h3> <a href='/home'>Home</a>")

def index(request):
    return HttpResponse("Hello rifat")

def home(request):
    return HttpResponse("<h3>Home</h3> <a href='/'>Welcome</a>")