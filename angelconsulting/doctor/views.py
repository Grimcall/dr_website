from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template import loader

def home_template(self, request : HttpRequest):
    nombre = request.POST.get("nombre")
    email = request.POST.get("email")
    mensaje = request.POST.get("mensaje")

def index(request : HttpRequest):
    return render(request, "index.html")


# Create your views here.
