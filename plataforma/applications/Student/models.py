from django.db import models

from datetime import datetime

from applications.User.choices import *
from applications.User.validators import *
from applications.User.models import *


class Estudiante(models.Model):
    codigo = models.CharField(unique=True, max_length=50, verbose_name='código')
    tDocument = models.ForeignKey(CatalogsTypesDocuement, on_delete=models.CASCADE, verbose_name='Tipo de documento')
    cedula = models.CharField(unique=False, max_length=20, verbose_name='Identificación del Estudiante', validators=[validate_cero])
    nombre = models.CharField(max_length=100, blank=False, null=False, verbose_name='Nombres')
    apellidos=models.CharField( verbose_name='Apellidos', max_length=100, blank=False, null=False)
    nacionalidad=models.CharField( verbose_name='Nacionalidad',max_length=100, choices=COUNTRIES, default="Colombia" )
    telefono=models.CharField( verbose_name='Teléfono', max_length=10, blank=False, null=False, validators=[validate_telefono])
    direccion=models.CharField( verbose_name='Direccion', max_length=50, blank=False, null=False)
    nacimiento=models.DateField( verbose_name='Fecha de Nacimiento', validators=[clean_nacimiento2])
    carrera=models.ForeignKey("Programs.Programas", on_delete=models.CASCADE)
    costo_cierre = models.DecimalField(max_digits= 25, decimal_places=0, default=0)
    email=models.EmailField( verbose_name='Em@il', blank=False, unique=False)
    sexo=models.CharField( verbose_name='sexo',max_length=50, choices=GENEROS, default="Femenino")
    sede=models.ForeignKey(CatalogsSede, verbose_name='Sede', on_delete=models.CASCADE)
    periodo_matriculado=models.ForeignKey("Programs.Periodos", verbose_name='Periodo', on_delete=models.CASCADE)
    fecha_reg=models.DateField(default=datetime.now, verbose_name='Fecha')
    updated_at = models.DateTimeField(auto_now=True)
    username=models.CharField(max_length=50, blank=False, null=False, verbose_name='Usuario', unique=True)
    nombre_acudiente = models.CharField(max_length=100, blank=False, null=False, verbose_name='Nombres del acudiente')
    apellidos_acudiente =models.CharField( verbose_name='Apellidos del acudiente', max_length=100, blank=False, null=False)
    telefono_acudiente =models.CharField( verbose_name='Teléfono del acudiente', max_length=10, blank=False, null=False, validators=[validate_telefono])
    cedula_acudiente =models.CharField(unique=False, max_length=20, verbose_name='Cédula del acudiente', validators=[validate_cero])
    document=models.BooleanField( default=False)
    simat=models.BooleanField(default=False)
    siet=models.BooleanField(default=False)
    actaBachillerato=models.BooleanField(default=False)
    fotos=models.BooleanField( default=False)
    serviciosPublicos=models.BooleanField(default=False)
    carneSalud=models.BooleanField(default=False)
    cedulaAcudiente=models.BooleanField( default=False)
    certificados=models.BooleanField(default=False)
    homologacion=models.BooleanField(default=False)
    observaciones=models.CharField(max_length=100, blank=True, null=True, verbose_name='Observacion')
    is_active=models.BooleanField(default=True)
    is_estudiante=models.BooleanField(default=True)
    is_matriculado=models.BooleanField(default=False)
    is_graduado=models.BooleanField(default=False)
    masivo=models.BooleanField(default=False)
    objects = BuscadorManager()
    
    def __str__(self): 
        
        return "{0}, {1}".format(self.apellidos, self.nombre)
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.fecha_reg = datetime.now()
        self.updated_at = datetime.now()
        return super(Estudiante, self).save(*args, **kwargs)
    