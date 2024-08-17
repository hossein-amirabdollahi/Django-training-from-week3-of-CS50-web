from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, "hello/index.html")

def hossein(request):
    return HttpResponse("Hello Hossein!")

def narges(request):
    return HttpResponse("Hello Narges!")

def greeting(request, name):
    return render(request, "hello/greeting.html", {
        "name": name.capitalize()
    })