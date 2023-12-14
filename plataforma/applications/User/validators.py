
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from datetime import date
from django.http import JsonResponse


def validate_cero(value):
    if value[0] == "0":
        raise ValidationError(
            _("El número de documento no puede comenzar por cero "),
            params={"value": value},
        )

def validate_decimal(value):
    if not float(value):
        raise ValidationError(
            _("La calificación %(value)s se encuentra en una notación que no es decimal, por favor modifiquela."),
            params={"value": value},
        )
    
def validate_telefono(value):
    tamaño = len(value)
    lista = [7, 10]
    if tamaño not in lista :
        raise ValidationError(
            _("El teléfono %(value)s  debe de tener 7 o 10 números"),
            params={"value": value},
        )
        
    
def validate_nacimiento(value):
    fecha_actual = date.today()
    fecha_final = ((fecha_actual - value).days)/365
    
    if fecha_final <= 17 :
        raise ValidationError(
            _("El docente no puede tener menos de 18 años, usted ingresó la fecha: %(value)s "),
            params={"value": value},
        )

def clean_nacimiento2(value):
    fecha_actual = date.today()
    fecha_final = ((fecha_actual - value).days)/365
    
    if fecha_final <= 13 :
        raise ValidationError(
            _("El Estudiante no puede tener menos de 13 años, usted ingresó la fecha: %(value)s "),
            params={"value": value},
        )
    
def validate_blanco(value):
    blancos = value.count(" ")
    
    if blancos > 0 :
        raise ValidationError(
            _("El nombre de usuario no puede tener espacios, verifique este valor %(value)s "),
            params={"value": value},
        )

