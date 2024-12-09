from django.db import models
from django.db.models import Max

from applications.User.models import *


from datetime import datetime


class CatalogsTypesInvoices(models.Model):
    estado = models.CharField(max_length=200, blank=True, null=True)
    def __str__(self):
        return self.estado
    
class CatalogsTypesGastos(models.Model):
    tipos = models.CharField(max_length=200, blank=True, null=True)
    def __str__(self):
        return self.tipos

class CatalogsTypesOtrosIngresos(models.Model):
    tipos = models.CharField(max_length=200, blank=True, null=True)
    def __str__(self):
        return self.tipos
    
class Facturas(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=200, blank=True, null=True)
    email=models.EmailField( verbose_name='Em@il', blank=True)
    monto =  models.DecimalField(max_digits= 30, decimal_places=0)
    due_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    descripcion = models.CharField(max_length=200, unique=False)
    estado = models.ForeignKey(CatalogsTypesInvoices, on_delete=models.CASCADE)
    objects = BuscadorManager()

    def __str__(self):
        return self.user

class FacturasSub(models.Model):
    facturas = models.ForeignKey(Facturas, on_delete=models.CASCADE, related_name='pagos')
    observacion=models.CharField(max_length=100, blank=True, null=True)
    consecutivo= models.PositiveIntegerField(null=False, blank=False, unique=True)
    pagado =  models.DecimalField(max_digits= 25, decimal_places=0, null=False, blank=False)
    created_at = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.facturas


class Gastos(models.Model):
    codigo = models.CharField(max_length=200, blank=True, null=True)
    consecutivo= models.PositiveIntegerField(null=False, blank=False, unique=True)
    descripcion = models.CharField(max_length=255, null=False, blank=False)
    monto = models.DecimalField(max_digits=25, decimal_places=2, null=False, blank=False)
    fecha = models.DateTimeField(default=datetime.now)
    tipo =  models.ForeignKey(CatalogsTypesGastos, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.codigo is None:
            max_codigo = Gastos.objects.aggregate(max_codigo=Max('codigo'))['max_codigo'] or 0
            self.codigo = int(max_codigo) + 1
        super().save(*args, **kwargs)

    


class OtroIngreso(models.Model):
    codigo = models.CharField(max_length=200, blank=True, null=True)
    consecutivo= models.PositiveIntegerField(null=False, blank=False, unique=True)
    descripcion = models.CharField(max_length=255, null=False, blank=False)
    monto = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    fecha = models.DateTimeField(default=datetime.now)
    tipo = models.ForeignKey(CatalogsTypesOtrosIngresos, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.codigo is None:
            max_codigo = OtroIngreso.objects.aggregate(max_codigo=Max('codigo'))['max_codigo'] or 0
            self.codigo = int(max_codigo) + 1
        super().save(*args, **kwargs)

