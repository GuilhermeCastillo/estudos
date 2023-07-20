from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def cars_view(request):
    return HttpResponse("<h1>Carros</h1>")
