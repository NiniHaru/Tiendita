from django.contrib import admin
from tiendita.models import Compra,Cliente, Detalle_compra, Producto


admin.site.register(Compra)
admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Detalle_compra)