from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import RESTRICT
from django.db.models.fields import BLANK_CHOICE_DASH, CharField
from .choices import tallas

class Persona(models.Model):
    per_rut=models.CharField(primary_key=True, max_length=10, blank=False)
    per_nombre=models.CharField(max_length=50, blank=False)
    per_apellido=models.CharField(max_length=50, blank=False)
    per_correo=models.CharField(max_length=30, blank=False, null=False)
    per_contra=models.CharField(max_length=24, blank=False, null=False)

    def __str__(self):
        return 'rut: %s, nombre: %s' %(self.per_rut,self.per_nombre)

    class Meta:
        abstract = True


class Admin(Persona):

    class Meta:
        verbose_name='Admin'
        verbose_name_plural='Admins'


class Cliente(Persona):
    cli_direccion=models.CharField(max_length=50, null=True, blank=False)
    cli_fono=models.IntegerField(blank=False)
    class Meta:
        verbose_name='Cliente'
        verbose_name_plural='Clientes'


class Vendedor(Persona):
    class Meta:
        verbose_name='Vendedor'
        verbose_name_plural='Vendedores'


class Producto(models.Model):
    pro_sku=models.CharField(primary_key=True, max_length=15,blank=False)
    pro_nombre=models.CharField(max_length=20, blank=False)
    pro_marca=models.CharField(max_length=30, blank=False, null=False)
    pro_precio=models.IntegerField(blank=False, null=False)
    pro_talla=models.CharField(max_length=3, blank=False, choices=tallas, default='TU')
    pro_comentario=models.CharField(max_length=40, blank=True, null=True)
    pro_categoria=models.CharField(max_length=50, blank=True)
    pro_disponibilidad=models.BooleanField(blank=False)
    pro_stock=models.IntegerField(blank=False, null=False)
    pro_imagen=models.ImageField(upload_to="fotos",blank=False, null=False)
    def __str__(self):
        return 'sku: %s, nombre: %s' %(self.pro_sku,self.pro_nombre)
    class Meta:
        verbose_name='Producto'
        verbose_name_plural='Productos'


class Detalle_compra(models.Model):
    com_id=models.IntegerField(primary_key=True)
    pro_sku=models.CharField(max_length=15, blank=False, null=False)
    det_com_cantidad=models.IntegerField(blank=False, null=False)
    det_com_precio=models.IntegerField(blank=False, null=False)
    det_com_producto = models.ForeignKey(Producto, null=False, blank=False, on_delete=RESTRICT)
    def __str__(self):
        return 'sku: %s, id: %s' %(self.pro_sku,self.com_id)
    class Meta:
        verbose_name='Detalle Compra'
        verbose_name_plural='Detalles Compra'


class Compra(models.Model):
    com_id=models.IntegerField(primary_key=True, blank=False)
    com_nroBoleta=models.IntegerField(blank=False)
    com_fecha=models.DateField(blank=False)
    com_direccionEnvio=models.CharField(max_length=50, blank=False)
    com_enviada=models.BooleanField(default=False)
    com_recibido=models.BooleanField(default=False)
    com_retiroTienda=models.BooleanField(default=False)
    com_recargo=models.IntegerField(blank=False, default=0)
    com_cliente=models.ForeignKey(Cliente, null=False, blank=False, on_delete=RESTRICT)
    com_detalles=models.ForeignKey(Detalle_compra, null=False, blank=False, on_delete=RESTRICT)
    def __str__(self):
        return 'nroBoleta: %s, fecha: %s' %(self.com_nroBoleta,self.com_fecha)
    class Meta:
        verbose_name='Compra'
        verbose_name_plural='Compras'



