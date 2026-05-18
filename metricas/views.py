from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):
    return HttpResponse("Estas en la app de metricas")

def resultados(request):
    return HttpResponse("Estas mirando los resultados de las metricas")

def errores(request):
    return HttpResponse("Esta es la pagina de error")