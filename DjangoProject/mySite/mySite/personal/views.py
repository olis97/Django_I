from django.shortcuts import render
from django.http import HttpResponse

def biography(request):
    return render(request, "mybio.html")

def token(request):
    return render(request, "token.html")

def token1(request):
    return render(request, "token1.html")