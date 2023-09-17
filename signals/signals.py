# signals.py
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Producto, Carrito
from django.core.cache import cache

@receiver(pre_save, sender=Carrito)
def producto_creado(sender, instance, **kwargs):    
    cache.delete('prod_added')
    print('Se actualizo el cache')