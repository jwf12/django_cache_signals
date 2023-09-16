from django.shortcuts import render
from django.views import generic
from .models import Producto
from django.views.decorators.cache import cache_page
from django.http import HttpResponse
import time

# Create your views here.
@cache_page(0, cache="default", key_prefix="prod_added")
#Funcion de PRUEBA para checkear con debug_TOOLBAR
def crearProducto(request):    
    productos = Producto.objects.all()
    return HttpResponse(f'<html><body><h1> {len(productos)} </h1></body></html>')