from django.db import models

from datetime import datetime
import uuid

from applications.User.choices import *
from applications.User.validators import *
from applications.User.models import *



class Docente(models.Model):
    slug = models.SlugField(unique=True, editable=False, blank=True)
    codigo = models.CharField(unique=True, max_length=50, verbose_name='código')
    tDocument = models.ForeignKey(CatalogsTypesDocuement, on_delete=models.CASCADE, verbose_name='Tipo de documento')
    nDocument = models.CharField(unique=True, max_length=20, verbose_name='Número de cédula', validators=[validate_cero])
    nombres = models.CharField(max_length=100, blank=False, null=False, verbose_name='Nombres')
    apellidos = models.CharField( max_length=100, blank=False, null=False, verbose_name='Apellidos')
    username=models.CharField(max_length=50, unique=True, blank=False, null=False, verbose_name='Usuario', validators=[validate_blanco])
    direccion = models.CharField( max_length=50, blank=False, null=False, verbose_name='dirección')
    nacionalidad=models.CharField( verbose_name='Nacionalidad',max_length=100, choices=COUNTRIES, default="Colombia" )
    nacimiento = models.DateField(verbose_name='Fecha de nacimiento', validators=[validate_nacimiento])
    sexo=models.CharField( verbose_name='Género',max_length=50, choices=GENEROS, default="Femenino")
    telefono = models.CharField(max_length=10, verbose_name='Teléfono', validators=[validate_telefono])
    email = models.EmailField() 
    fecha_reg=models.DateField(default=datetime.now, verbose_name='Fecha')
    is_active=models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BuscadorManager()

    def __str__(self): 
        return self.nombres + " " + self.apellidos
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.fecha_reg = datetime.now()
        self.updated_at = datetime.now()

        # Generar un slug único al guardar el objeto
        if not self.slug:
            self.slug = str(uuid.uuid4())
        return super(Docente, self).save(*args, **kwargs)
