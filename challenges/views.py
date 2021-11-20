from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def january(request):
    return HttpResponse('This in january, Always dream your dream!')


def february(request):
    return HttpResponse('This is february, Work smart and earn better!')

def march(request):
    return HttpResponse('This is march, Run with the phase, do not stop when you fail!')