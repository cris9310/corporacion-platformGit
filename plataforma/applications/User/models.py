from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from datetime import datetime

from .manager import *
from .validators import *

#Con estos primeros 5 modelos lo que hacemos es crear catálogos para los choices y hacer la app más escalable
class CatalogsTypesProg(models.Model):
    tipo = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self): 
        return  self.tipo

class CatalogsTypesActivities(models.Model):
    tipo = models.CharField(max_length=200, null=False, blank=False)
    observaciones=models.CharField(max_length=100, blank=True, null=True, verbose_name='Observacion')

    def __str__(self): 
        return  self.tipo

class CatalogsTypesDocuement(models.Model):
    tipo = models.CharField(max_length=200, null=False, blank=False)
    nombre = models.CharField(max_length=200, null=False, blank=False)


    def __str__(self): 
        return  self.nombre
    
class CatalogsTypesRol(models.Model):
    rol = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self): 
        return  self.rol

class CatalogsSede(models.Model):
    sede= models.CharField(max_length=200, null=False, blank=False)

    def __str__(self): 
        return  self.sede


#Modelo de los usuarios, se reescribió todo el modelo inicial e hicimos uno desde cero, logueamos con user y contraseña
class User(AbstractBaseUser):
    codigo=models.CharField(primary_key=True, max_length=20, unique=True, verbose_name='Código')
    nombres = models.CharField(max_length=50, blank=False, null=True)
    apellidos = models.CharField(max_length=50, blank=False, null=True)
    username=models.CharField(max_length=50, unique=True, blank=False, null=False, verbose_name='Usuario')
    email=models.EmailField( verbose_name='Em@il', blank=False)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(auto_now=True)
    tipe = models.ForeignKey(CatalogsTypesRol, on_delete=models.CASCADE)
    is_superuser=models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    objects= ManagerUsers()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS= ["nombres", "apellidos", "email","tipe"]
    

    def get_short_name(self):
        return self.username

    class Meta:
        ordering = ('-created_at', '-updated_at', )
    
    def has_perm(self, perm, obj=None):
        return True
    def has_module_perms(self, app_label):
        return True
    
