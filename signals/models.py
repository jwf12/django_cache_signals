from django.db import models
from shortuuid.django_fields import ShortUUIDField

# Create your models here.
class Producto(models.Model):
    name = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    number = ShortUUIDField(length=6)
    
    def __str__(self):
        return self.name

class Carrito(models.Model):
    name = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    number = ShortUUIDField(length=6)
    count = models.IntegerField(default=1)

    def __str__(self):
        return self.name

