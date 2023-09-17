from django.contrib import admin
from .models import Producto, Carrito


class ProductoRegister(admin.ModelAdmin):
    list_display=[
        'name',
        'number'
    ]
# Register your models here.
admin.site.register(Producto,ProductoRegister)
admin.site.register(Carrito,ProductoRegister)