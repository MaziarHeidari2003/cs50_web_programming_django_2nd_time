from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request): # the http request that the user made in order to acces the web server
  return render(request, "hello/index.html")

def maziar(request):
  return HttpResponse('Hello maziar')

def messi(request):
  return HttpResponse('Hello messi')

def greet(request, name):
  return render(request, "hello/greet.html", {
    "name": name.capitalize()
  })