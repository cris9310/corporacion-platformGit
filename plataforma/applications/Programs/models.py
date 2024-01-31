from django.db import models

from datetime import datetime



from applications.User.choices import *
from applications.User.validators import *
from applications.User.models import *
from applications.Teacher.models import *
from applications.Student.models import *

class Periodos(models.Model):
    periodo = models.CharField(max_length=15, unique=True, blank=False, null=False)
    an_creacion=models.DateTimeField(default=datetime.now)
    objects = periodoManager()

    def __str__(self): 
        return self.periodo
    
    class Meta:
       ordering = ('-an_creacion', )

class Programas(models.Model):
    cod_prog=models.CharField(max_length=10, unique=True, verbose_name='Código del Programa')
    programa_name=models.CharField(max_length=100, blank=False, null=False, verbose_name='Nombre del Programa')
    aceptado = models.PositiveIntegerField(null=False, blank=False, verbose_name='Total materias', validators=[validate_noncero])
    matricula = models.DecimalField(max_digits= 25, decimal_places=0, default=0, verbose_name='Valor de la matrícula', validators=[validate_noncero])
    derechosGrado = models.DecimalField(max_digits= 35, decimal_places=0, default=0, verbose_name='Valor de derechos a grado' , validators=[validate_noncero])
    cuota_valor= models.DecimalField(max_digits= 25, decimal_places=0, default=0, verbose_name='Valor de la mensualidad', validators=[validate_noncero])
    cuotas= models.PositiveIntegerField(null=False, blank=False, verbose_name='Número de cuotas', validators=[validate_noncero])
    costo =  models.DecimalField(max_digits= 25, decimal_places=0, default=0)
    an_creacion=models.CharField(max_length=50, default=datetime.now)
    updated_at = models.DateTimeField(auto_now=True)
    tipe = models.ForeignKey(CatalogsTypesProg, on_delete=models.CASCADE)
    is_active=models.BooleanField(default=True)
    objects = BuscadorManager()

    def __str__(self): 
        return  self.programa_name


class Inventario(models.Model):
    codigo = models.CharField(max_length=200, null=False, blank=False, verbose_name='Código de la asignatura')
    nombre_materia = models.CharField(max_length=200, null=False, blank=False, verbose_name='Nombre de la Asignatura')
    programa = models.ForeignKey(Programas, on_delete=models.CASCADE)
    an_creacion=models.CharField(max_length=50, default=datetime.now) 
    updated_at = models.DateTimeField(auto_now=True)
    objects = BuscadorManager()

    def __str__(self): 
        return  self.nombre_materia
    

class Materias(models.Model):

    materia  = models.ForeignKey(Inventario, on_delete=models.CASCADE )
    sede=models.ForeignKey(CatalogsSede, verbose_name='Sede', on_delete=models.CASCADE)
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE )
    periodo = models.ForeignKey(Periodos, on_delete=models.CASCADE)
    jornada = models.ForeignKey(CatalogsJornada, on_delete=models.CASCADE)
    pre_cierre =models.DateField()
    cierre =models.DateField()
    an_creacion=models.CharField(max_length=50, default=datetime.now)
    updated_at = models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)
    objects = BuscadorManager()


    class Meta:
        ordering = ['materia']
    
    def __str__(self): 
        return self.materia

class Banner(models.Model):
    student = models.ForeignKey(Estudiante, verbose_name='Estudiante', on_delete=models.CASCADE)
    materia = models.ForeignKey(Materias, verbose_name='Materias', on_delete=models.CASCADE)
    tarea = models.ForeignKey(CatalogsTypesActivities, verbose_name='Tareas', on_delete=models.CASCADE)
    cod_tarea=models.CharField(max_length=20, default=0000 )
    calificacion = models.DecimalField(max_digits = 5, decimal_places = 2, verbose_name='Calificacion')
    observacion = models.CharField(max_length=200, blank=False)
    objects = BuscadorManager()

    class Meta:
        ordering = ['cod_tarea']
