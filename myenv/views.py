from django.http.request import HttpRequest
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("home")

def about(request):
    return HttpResponse("about")

def blog(request):
    return HttpResponse("blog")

def contact(request):
    return HttpResponse("contact")