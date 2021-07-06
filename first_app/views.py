from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# here is my first django comment

def index(request):
    diction = {'name':'Rifat al mamun'}

    return render(request, 'first_app/index.html', context=diction)

    
def home(request):
    return HttpResponse("<h3>Home</h3> <a href='/first_app'>first app index</a>")