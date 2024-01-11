from django.forms import *
from django import forms


from .models import *



class StudentRegisterForm(forms.ModelForm):

    
    class Meta:
        
        model = Estudiante
        fields = ('__all__')
        exclude =['is_estudiante','is_active', 'fecha_reg', 
                  'is_matriculado','codigo', 'is_graduado', 
                  'costo_cierre', "masivo", "updated_at"
                ]
        
        widgets={

            'cedula': NumberInput(
                attrs={
                    'autocomplete': 'off',
                    'class':'form-control',
                    'id':'cedula',
                    'placeholder':"Ingrese número de documento",
                    "onkeydown":"noPuntoComa( event )"
                }
            ),
            'tDocument': Select(
                attrs={
                    'autocomplete': 'off',
                    'class':'form-control',
                    "id": "tDocument"
                }
            ),
            'nombre': TextInput(
                attrs={
                    'placeholder':"Ingrese nombres",
                    'autocomplete': 'off',
                    'class':'form-control ',
                    'id': 'nombre'
                }
            ),
            'apellidos': TextInput(
                attrs={
                    'placeholder':"Ingrese apellidos",
                    'autocomplete': 'off',
                    'class':'form-control ',
                    'id': 'apellidos'
                }
            ),
            'direccion': TextInput(
                attrs={
                    'placeholder':"Ingrese dirección",
                    'autocomplete': 'off',
                    'class':'form-control ',
                    'id': 'direccion'
                }
            ),

            'telefono': NumberInput(
                attrs={
                    'placeholder':"Ingrese teléfono",
                    'autocomplete': 'off',
                    'class':'form-control ',
                    'id': 'telefono',
                    "onkeydown":"noPuntoComa( event )"
                }
            ),

            'sexo': Select(
                attrs={
                    'autocomplete': 'off',
                    'class':'form-control',
                    'id': 'sexo'
                }
            ),
            'nacionalidad': Select(
                attrs={
                    'autocomplete': 'off',
                    'class':'form-control ',
                    'id': 'nacionalidad'
                }
            ),
            'nacimiento': DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'type':'date',
                    'class':'form-control',
                    'id': 'nacimiento'
                }
            ),
            'email': EmailInput(
                attrs={
                    'placeholder':"Ingrese correo electrónico",
                    'autocomplete': 'off',
                    'class':'form-control ',
                    'id': 'email'
                }
            ),
            'username': TextInput(
                attrs={
                    'placeholder':"Ingrese un nombre de usuario",
                    'autocomplete': 'off',
                    'class':'form-control ',
                    'id': 'username'
                }
            ),

            'nombre_acudiente': TextInput(
                attrs={
                    'autocomplete': 'off',
                    'class':'form-control ',
                    'placeholder':"Ingrese nombre del acudiente",
                    'id': 'nombre_acudiente'
                }
            ),
            'apellidos_acudiente': TextInput(
                attrs={
                    'autocomplete': 'off',
                    'placeholder':"Ingrese apellidos del acudiente",
                    'class':'form-control ',
                    'id': 'apellidos_acudiente'

                }
            ),
            'telefono_acudiente': NumberInput(
                attrs={
                    
                    'autocomplete': 'off',
                    'class':'form-control ',
                    'placeholder':"Ingrese teléfono de contacto",
                    'id': 'telefono_acudiente',
                    "onkeydown":"noPuntoComa( event )"


                }
            ),

            'cedula_acudiente': NumberInput(
                attrs={
                    'autocomplete': 'off',
                    'class':'form-control ',
                    'placeholder':"Ingrese documento del acudiente",
                    'id': 'cedula_acudiente',
                    "onkeydown":"noPuntoComa( event )"


                }
            ),


            'periodo_matriculado': Select(
                attrs={
                    'autocomplete': 'off',
                    'class':'form-control',
                    'id': 'periodo_matriculado'

                }
            ),
            
            'carrera': Select(
                attrs={
                    'autocomplete': 'off',
                    'class':'form-control ',
                    'id':'carrera'
                }
            ),
            
            'sede': Select(
                    attrs={
                        'autocomplete': 'off',
                        'class':'form-control ',
                        'id': 'sede'

                    }
            ),
            'document': CheckboxInput(
                    attrs={
                        'class':'form-check-input',
                        'id': 'document'

                    }
            ),
            'fotos': CheckboxInput(
                    attrs={
                        'class':'form-check-input',
                        'id': 'fotos'

                    }
            ),
            'siet': CheckboxInput(
                    attrs={
                        'class':'form-check-input',
                        'id': 'siet'

                    }
            ),
            'actaBachillerato': CheckboxInput(
                    attrs={
                        'class':'form-check-input',
                        'id': 'actaBachillerato'

                    }
            ),
            'serviciosPublicos': CheckboxInput(
                    attrs={
                        'class':'form-check-input',
                        'id': 'serviciosPublicos'

                    }
            ),
            'carneSalud': CheckboxInput(
                    attrs={
                        'class':'form-check-input',
                        'id': 'carneSalud'

                    }
            ),
            'cedulaAcudiente': CheckboxInput(
                    attrs={
                        'class':'form-check-input',
                        'id': 'cedulaAcudiente'

                    }
            ),
            'certificados': CheckboxInput(
                    attrs={
                        'class':'form-check-input',
                        'id': 'certificados'

                    }
            ),
            'homologacion': CheckboxInput(
                    attrs={
                        'class':'form-check-input',
                        'id': 'homologacion'

                    }
            ),
            'observaciones': Textarea(
                attrs={
                    'autocomplete': 'off',
                    'class':'form-control ',
                    'id': 'observaciones'
                }
            ),
        }
    
    def clean_nombre(self):

        nombre = str(self.cleaned_data.get('nombre'))

        return nombre.title()


    def clean_apellidos(self):

        nombre = str(self.cleaned_data.get('apellidos'))

        return nombre.title()
    
    def clean_nombre_acudiente(self):
        nombre = str(self.cleaned_data.get('nombre_acudiente'))

        return nombre.title()

    def clean_apellidos_acudiente(self):
        nombre = str(self.cleaned_data.get('apellidos_acudiente'))

        return nombre.title()
    
    def clean_username(self):
        if User.objects.filter(username=self.cleaned_data.get('username')):
           
           self.add_error('username', 'Este usuario ya se encuentra creado')
        else:
           return self.cleaned_data.get('username')


class StudentUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(StudentUpdateForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance.id:
            self.fields['carrera'].widget.attrs['disabled'] = 'disabled'
            self.fields['username'].widget.attrs['disabled'] = 'disabled'
    
    class Meta:
        
        model = Estudiante
        fields = ('__all__')
        exclude =['is_estudiante','is_active', 'fecha_reg', 
                  'is_matriculado','codigo', 'is_graduado', 
                  'costo_cierre', "masivo", "updated_at"
                ]
        
        widgets={

            'cedula': NumberInput(
                attrs={
                    'autocomplete': 'off',
                    'class':'form-control',
                    'id':'cedula',
                    'placeholder':"Ingrese número de documento",
                    "onkeydown":"noPuntoComa( event )"
                }
            ),
            'tDocument': Select(
                attrs={
                    'autocomplete': 'off',
                    'class':'form-control',
                    "id": "tDocument"
                }
            ),
            'nombre': TextInput(
                attrs={
                    'placeholder':"Ingrese nombres",
                    'autocomplete': 'off',
                    'class':'form-control ',
                    'id': 'nombre'
                }
            ),
            'apellidos': TextInput(
                attrs={
                    'placeholder':"Ingrese apellidos",
                    'autocomplete': 'off',
                    'class':'form-control ',
                    'id': 'apellidos'
                }
            ),
            'direccion': TextInput(
                attrs={
                    'placeholder':"Ingrese dirección",
                    'autocomplete': 'off',
                    'class':'form-control ',
                    'id': 'direccion'
                }
            ),

            'telefono': NumberInput(
                attrs={
                    'placeholder':"Ingrese teléfono",
                    'autocomplete': 'off',
                    'class':'form-control ',
                    'id': 'telefono',
                    "onkeydown":"noPuntoComa( event )"
                }
            ),

            'sexo': Select(
                attrs={
                    'autocomplete': 'off',
                    'class':'form-control',
                    'id': 'sexo'
                }
            ),
            'nacionalidad': Select(
                attrs={
                    'autocomplete': 'off',
                    'class':'form-control ',
                    'id': 'nacionalidad'
                }
            ),
            'nacimiento': DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'type':'date',
                    'class':'form-control',
                    'id': 'nacimiento'
                }
            ),
            'email': EmailInput(
                attrs={
                    'placeholder':"Ingrese correo electrónico",
                    'autocomplete': 'off',
                    'class':'form-control ',
                    'id': 'email'
                }
            ),
            'username': TextInput(
                attrs={
                    'placeholder':"Ingrese un nombre de usuario",
                    'autocomplete': 'off',
                    'class':'form-control ',
                    'id': 'username'
                }
            ),

            'nombre_acudiente': TextInput(
                attrs={
                    'autocomplete': 'off',
                    'class':'form-control ',
                    'placeholder':"Ingrese nombre del acudiente",
                    'id': 'nombre_acudiente'
                }
            ),
            'apellidos_acudiente': TextInput(
                attrs={
                    'autocomplete': 'off',
                    'placeholder':"Ingrese apellidos del acudiente",
                    'class':'form-control ',
                    'id': 'apellidos_acudiente'

                }
            ),
            'telefono_acudiente': NumberInput(
                attrs={
                    
                    'autocomplete': 'off',
                    'class':'form-control ',
                    'placeholder':"Ingrese teléfono de contacto",
                    'id': 'telefono_acudiente',
                    "onkeydown":"noPuntoComa( event )"


                }
            ),

            'cedula_acudiente': NumberInput(
                attrs={
                    'autocomplete': 'off',
                    'class':'form-control ',
                    'placeholder':"Ingrese documento del acudiente",
                    'id': 'cedula_acudiente',
                    "onkeydown":"noPuntoComa( event )"


                }
            ),


            'periodo_matriculado': Select(
                attrs={
                    'autocomplete': 'off',
                    'class':'form-control',
                    'id': 'periodo_matriculado'

                }
            ),
            
            'carrera': Select(
                attrs={
                    'autocomplete': 'off',
                    'class':'form-control ',
                    'id':'carrera'
                }
            ),
           
            'sede': Select(
                    attrs={
                        'autocomplete': 'off',
                        'class':'form-control ',
                        'id': 'sede'

                    }
                ),
            'document': CheckboxInput(
                    attrs={
                        'class':'form-check-input',
                        'id': 'document'

                    }
            ),
            'fotos': CheckboxInput(
                    attrs={
                        'class':'form-check-input',
                        'id': 'fotos'

                    }
            ),
            'siet': CheckboxInput(
                    attrs={
                        'class':'form-check-input',
                        'id': 'siet'

                    }
            ),
            'actaBachillerato': CheckboxInput(
                    attrs={
                        'class':'form-check-input',
                        'id': 'actaBachillerato'

                    }
            ),
            'serviciosPublicos': CheckboxInput(
                    attrs={
                        'class':'form-check-input',
                        'id': 'serviciosPublicos'

                    }
            ),
            'carneSalud': CheckboxInput(
                    attrs={
                        'class':'form-check-input',
                        'id': 'carneSalud'

                    }
            ),
            'cedulaAcudiente': CheckboxInput(
                    attrs={
                        'class':'form-check-input',
                        'id': 'cedulaAcudiente'

                    }
            ),
            'certificados': CheckboxInput(
                    attrs={
                        'class':'form-check-input',
                        'id': 'certificados'

                    }
            ),
            'homologacion': CheckboxInput(
                    attrs={
                        'class':'form-check-input',
                        'id': 'homologacion'

                    }
            ),
            'observaciones': Textarea(
                attrs={
                    'autocomplete': 'off',
                    'class':'form-control ',
                    'id': 'observaciones'
                }
            ),

        }
    
    def clean_nombre(self):

        nombre = str(self.cleaned_data.get('nombre'))

        return nombre.title()


    def clean_apellidos(self):

        nombre = str(self.cleaned_data.get('apellidos'))

        return nombre.title()
    
    def clean_nombre_acudiente(self):
        nombre = str(self.cleaned_data.get('nombre_acudiente'))

        return nombre.title()

    def clean_apellidos_acudiente(self):
        nombre = str(self.cleaned_data.get('apellidos_acudiente'))

        return nombre.title()
    

#Formulario de cargue masivo de estudiantes.
class StudentAsigMate(forms.Form):

    carga = forms.FileField(
        required=True,
        widget=forms.FileInput(
            attrs={
                'class':'form-control ',
                'name':'carga',
                'id':'carga'

            }
        )
    )

    def clean_carga(self):
        carga_file1 = self.cleaned_data['carga'].name
        carga_file_exp = (self.files['carga'])

        if carga_file1 != 'cargue_estudiantes.xlsx' :
           self.add_error('carga', 'Archivo inválido, recuerde que el archivo tiene por nombre "cargue_estudiantes.xlsx" , por favor verifique y cárguelo nuevamente')

        else:
            return carga_file_exp
        

#Formulario de cargue masivo de estudiantes.
class StudentAsigNewForm(forms.Form):

    asignaturas = forms.HiddenInput(
        attrs={
                'id':'asignaturas'
            }
    ),

    estudiante = forms.HiddenInput(
        attrs={
                'id':'estudiante'
        }
    )