from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# here is my first django comment

def index(request):
    return HttpResponse("<h3>First App Index</h3> <a href='/first_app/home'>first app Home</a>")

def home(request):
    return HttpResponse("<h3>Home</h3> <a href='/first_app'>first app index</a>")