from django.db import models

from applications.User.models import *
from applications.User.manager import *


class CatalogsTypesInvoices(models.Model):
    estado = models.CharField(max_length=200, blank=True, null=True)
    def __str__(self):
        return self.estado

    
class Facturas(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=200, blank=True, null=True)
    email=models.EmailField( verbose_name='Em@il', blank=True)
    monto =  models.DecimalField(max_digits= 30, decimal_places=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    descripcion = models.CharField(max_length=200, unique=False)
    estado = models.ForeignKey(CatalogsTypesInvoices, on_delete=models.CASCADE)
    objects = BuscadorManager()

    def __str__(self):
        return self.user

class FacturasSub(models.Model):
    facturas = models.ForeignKey(Facturas, on_delete=models.CASCADE)
    observacion=models.CharField(max_length=100, blank=True, null=True)
    consecutivo= models.PositiveIntegerField(null=False, blank=False, unique=True)
    pagado =  models.DecimalField(max_digits= 100, decimal_places=0)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.facturas

class Gastos(models.Model):
    consecutivo= models.PositiveIntegerField(null=False, blank=False, unique=True)
    def __str__(self):
        return self.consecutivo
