from django.forms import *
from django import forms



from .models import *


#Formulario destinado a la creación de docentes está ok
class TeacherForm(forms.ModelForm):


    class Meta:
        """Meta definition for MODELNAMEform."""

        model = Docente
        fields = ('__all__')
        exclude =['fecha_reg', 'is_active']

        widgets={

            'nacimiento': DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'type':'date',
                    'class':'form-control',
                    'id': 'nacimiento'
                }
            ),
            'nacionalidad': Select(
                attrs={
                    'autocomplete': 'off',
                    'class':'form-control ',
                    'id': 'nacionalidad'
                }
            ),

             'tDocument': Select(
                attrs={
                    'autocomplete': 'off',
                    'class':'form-control',
                    "id": "tDocument"
                }
            ),

            'codigo': NumberInput(
                attrs={
                    'autofocus': True,
                    'placeholder':"Ingrese el documento",
                    'autocomplete': 'off',
                    'class':'form-control',
                    "onkeydown":"noPuntoComa( event )",
                    'id':'cedula'
                    
                }
            ),
            'nombres': TextInput(
                attrs={
                    'placeholder':"Ingrese nombres",
                    'autocomplete': 'off',
                    'class':'form-control',
                    'id': 'nombres'
                }
            ),
            'apellidos': TextInput(
                attrs={
                    'placeholder':"Ingrese apellidos",
                    'autocomplete': 'off',
                    'class':'form-control',
                    'id': 'apellidos'
                }
            ),
            'username': TextInput(
                attrs={
                    'placeholder':"nombre de usuario",
                    'autocomplete': 'off',
                    'class':'form-control',
                    'id': 'username'
                }
            ),
            

            'direccion': TextInput(
                attrs={
                    'placeholder':"nombre dirección",
                    'autocomplete': 'off',
                    'class':'form-control',
                    'id': 'direccion'
                }
            ),

            'telefono': NumberInput(
                attrs={
                    'placeholder':"Ingrese teléfono",
                    'autocomplete': 'off',
                    'class':'form-control',
                    "onkeydown":"noPuntoComa( event )",
                    'id': 'telefono',
                }
            ),

            'email': EmailInput(
                attrs={
                    'placeholder':"Ingrese correo electrónico",
                    'autocomplete': 'off',
                    'class':'form-control',
                    'id': 'email',
                }
            ),
            'sexo': Select(
                attrs={
                    'autocomplete': 'off',
                    'class':'form-control',
                    'id': 'sexo'
                }
            ),

        }
    
    def clean_nombres(self):

        nombre = str(self.cleaned_data.get('nombres'))

        return nombre.title()

    def clean_apellidos(self):

        nombre = str(self.cleaned_data.get('apellidos'))

        return nombre.title()
    
    def clean_username(self):
        if User.objects.filter(username=self.cleaned_data.get('username')):
           
           self.add_error('username', 'Este usuario ya se encuentra creado')
        else:
           return self.cleaned_data.get('username')

# Formulario para la actualización de los datos del docente
class TeacherUpdateForm(forms.ModelForm):


    class Meta:
        """Meta definition for MODELNAMEform."""

        model = Docente
        fields = ('__all__')
        exclude =['fecha_reg', 'is_active', 'username']

        widgets={

            'nacimiento': DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'type':'date',
                    'class':'form-control',
                    'id': 'nacimiento'
                }
            ),
            'nacionalidad': Select(
                attrs={
                    'autocomplete': 'off',
                    'class':'form-control ',
                    'id': 'nacionalidad'
                }
            ),

             'tDocument': Select(
                attrs={
                    'autocomplete': 'off',
                    'class':'form-control',
                    "id": "tDocument"
                }
            ),

            'codigo': NumberInput(
                attrs={
                    'autofocus': True,
                    'placeholder':"Ingrese el documento",
                    'autocomplete': 'off',
                    'class':'form-control',
                    "onkeydown":"noPuntoComa( event )",
                    'id':'cedula'
                    
                }
            ),
            'nombres': TextInput(
                attrs={
                    'placeholder':"Ingrese nombres",
                    'autocomplete': 'off',
                    'class':'form-control',
                    'id': 'nombres'
                }
            ),
            'apellidos': TextInput(
                attrs={
                    'placeholder':"Ingrese apellidos",
                    'autocomplete': 'off',
                    'class':'form-control',
                    'id': 'apellidos'
                }
            ),
            

            'direccion': TextInput(
                attrs={
                    'placeholder':"nombre dirección",
                    'autocomplete': 'off',
                    'class':'form-control',
                    'id': 'direccion'
                }
            ),

            'telefono': NumberInput(
                attrs={
                    'placeholder':"Ingrese teléfono",
                    'autocomplete': 'off',
                    'class':'form-control',
                    "onkeydown":"noPuntoComa( event )",
                    'id': 'telefono',
                }
            ),

            'email': EmailInput(
                attrs={
                    'placeholder':"Ingrese correo electrónico",
                    'autocomplete': 'off',
                    'class':'form-control',
                    'id': 'email',
                }
            ),
            'sexo': Select(
                attrs={
                    'autocomplete': 'off',
                    'class':'form-control',
                    'id': 'sexo'
                }
            ),

        }
    
    def clean_nombres(self):

        nombre = str(self.cleaned_data.get('nombres'))

        return nombre.title()

    def clean_apellidos(self):

        nombre = str(self.cleaned_data.get('apellidos'))

        return nombre.title()

  

