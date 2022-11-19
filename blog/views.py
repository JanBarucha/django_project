from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1> Blog Homeeeee </h1>')



def about(request):
    return HttpResponse(
        '<h1> We are in about view </h1>'
    )