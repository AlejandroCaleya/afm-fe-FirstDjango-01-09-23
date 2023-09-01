from django.urls import path
from . import views

urlpatterns = [
    path('', views.bienvenida, name='bienvenida'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contacto'),
]