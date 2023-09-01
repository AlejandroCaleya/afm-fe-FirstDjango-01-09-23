from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def bienvenida(request):
    return render(request,'home.html')

def about(request):
    return HttpResponse('<h3>Bienvenido a la página Acerca de Nosotros</h3>')

def contact(request):
    return HttpResponse('<h3>Bienvenido a la página de Contacto</h3>')