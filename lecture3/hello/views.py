from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request): # the http request that the user made in order to acces the web server
  return HttpResponse("Hello world")
