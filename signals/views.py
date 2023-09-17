from typing import Any
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from .models import *

from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator


from django.db.models import F



class ListarProductos(generic.ListView):
    model = Producto
    template_name = 'index.html'
    context_object_name = 'productos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["carritos"] = Carrito.objects.all()
        return context
    


class CrearProductos(generic.ListView):
    model = Producto
    template_name = 'index.html'

    
    def get(self, request, *args, **kwargs):
        producto_id = self.kwargs['producto_id']
        producto = Producto.objects.get(pk=producto_id)
        
        #Busco si el producto existe en el carrito
        carrito_obj = Carrito.objects.filter(number=producto.number).first()

        #si existe el objeto, agrega uno al count
        if carrito_obj:
            carrito_obj.count=F('count') + 1
            carrito_obj.save()
        #si no existe lo creo
        else:
            Carrito.objects.create(name=producto.name, precio=producto.precio, number=producto.number)

        return redirect('signals:home')
    
     


#Funcion de PRUEBA para checkear con debug_TOOLBAR
#@cache_page(0, cache='default', key_prefix="prod_added")
# def crearProducto(request):    
#     productos = Producto.objects.all()
#     return HttpResponse(f'<html><body><h1> {len(productos)} </h1></body></html>')