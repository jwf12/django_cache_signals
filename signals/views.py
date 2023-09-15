from django.shortcuts import render
from django.views import generic
from .models import Producto
from django.views.decorators.cache import cache_page
from django.http import HttpResponse

# Create your views here.
@cache_page(60*1)
def crearProducto(request):    
    productos= Producto.objects.all()
    return HttpResponse('<html><body><h1> {0} </h1></body></html>'.format(len(productos)))