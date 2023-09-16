# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Producto
from django.core.cache import cache

@receiver(post_save, sender=Producto)
def producto_creado(sender, instance, **kwargs):
    
    cache.delete('prod_added')
    print('Se actualizo el cache')