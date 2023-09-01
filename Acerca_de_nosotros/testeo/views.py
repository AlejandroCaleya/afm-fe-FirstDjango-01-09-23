from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def testeo(request):
    html= '''
    <h1>Hola mundo</h1>

    <ul>
    <li><a href='/'>Bienvenida</a></li>
    <li><a href='/about/'>About</a></li>
    <li><a href='/contact/'>Contact</a></li>
    </ul>
    '''
    return HttpResponse(html)
