from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('hello there')

def about(request):
    return HttpResponse('This is the about page')

