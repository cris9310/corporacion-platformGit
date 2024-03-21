from django.forms import *
from django import forms




##Formulario de creacion de periodos
class ContactForm(forms.Form):

    nombre = forms.CharField(
        label='Nombre(s)',
        required=True,
        widget=forms.TextInput(
            attrs={
                    
                    'autocomplete': 'off',
                    'class':'form-control ',
                    'id': 'nombre',
                    'placeholder':"Introduce tu nombre"
            }
        )

    )

    apellidos = forms.CharField(
        label='Apellidos',
        required=True,
        widget=forms.TextInput(
            attrs={
                    
                    'autocomplete': 'off',
                    'class':'form-control ',
                    'id': "apellidos",
                    'placeholder':"Ingrese tus apellidos"
            }
        )

    )


    email = forms.CharField(
        label='Correo electrónico',
        required=True,
        widget=forms.EmailInput(
            attrs={
                    
                    'autocomplete': 'off',
                    'class':'form-control ',
                    'id': "email",
                    'placeholder':"Ingrese su correo electrónico"
            }
        )

    )

    telefono = forms.CharField(
        label='Teléfono de contacto',
        required=True,
        widget=forms.TextInput(
            attrs={
                    
                    'autocomplete': 'off',
                    'class':'form-control ',
                    'id': "telefono",
                    'placeholder':"Ingrese un teléfono de contacto"
            }
        )

    )

    observacion = forms.CharField(
        label='Observaciones',
        required=True,
        widget=forms.Textarea(
            attrs={
                    
                    'autocomplete': 'off',
                    'class':'form-control ',
                    'id': "observacion",
                    'placeholder':"¿En qué podemos ayudarte?"
            }
        )

    )




