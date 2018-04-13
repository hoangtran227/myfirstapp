from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def page1(request):
    return HttpResponse("Day la page 1")
def page2(request):
    return HttpResponse("Day la page 2")