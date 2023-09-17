from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page

app_name='signals'

urlpatterns = [
    path('', ListarProductos.as_view(), name='home'),
    path('crear/<int:producto_id>/', cache_page(0, cache='default', key_prefix="prod_added")(CrearProductos.as_view()), name='crear'),

]
