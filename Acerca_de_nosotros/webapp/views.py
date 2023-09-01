from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def bienvenida(request):
    return HttpResponse('<h1>Bienvenido a la página principal</h1>')

def about(request):
    return HttpResponse('<h3>Bienvenido a la página Acerca de Nosotros</h3>')

def contact(request):
    return HttpResponse('<h3>Bienvenido a la página de Contacto</h3>')