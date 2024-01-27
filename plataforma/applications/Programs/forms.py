from django.forms import *
from django import forms

from .models import *

##Formulario de creacion de periodos
class PeriodoForm(forms.ModelForm):

    anio = forms.CharField(
        label='Año',
        required=True,
        widget=forms.NumberInput(
            attrs={
                    
                    'autocomplete': 'off',
                    'class':'form-control ',
                    'id': 'anio',
                    'placeholder':"Ingrese el año",
                    "onkeydown":"noPuntoComa( event )"
            }
        )

    )

    periodo = forms.CharField(
        label='Periodo',
        required=True,
        widget=forms.NumberInput(
            attrs={
                    
                    'autocomplete': 'off',
                    'class':'form-control ',
                    'id': "periodo",
                    'placeholder':"Ingrese el periodo",
                    "onkeydown":"noPuntoComa( event )"
            }
        )

    )

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = Periodos
        fields = ('__all__')
        exclude =['an_creacion', "periodo"]

    def clean_periodo(self):
        ano = self.cleaned_data.get('anio')
        periodo = self.cleaned_data.get('periodo')
        concat=str(ano) + "-" + periodo
        
        if Periodos.objects.filter(periodo = concat).exists() :
           self.add_error('anio', 'El periodo que intenta crear ya existe.')
        else:
            return concat



class ProgramaForm(forms.ModelForm):

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = Programas
        fields = ('__all__')
        exclude =['an_creacion', 'is_active', 'cod_prog', 'is_active' ]



        widgets={

            'programa_name': TextInput(
                attrs={
                    'id':'programa_name',
                    'placeholder':"Ingrese un nombre",
                    'autocomplete': 'off',
                    'class':'form-control'
                }
            ),
            "aceptado": NumberInput(
                attrs={
                    'id':'aceptado',
                    'placeholder':"Ingrese un valor",
                    'autocomplete': 'off',
                    'class':'form-control',
                     "onkeydown":"noPuntoComa( event )"
                }
            ),
            "matricula":NumberInput(
                attrs={
                    'id':'matricula',
                    'placeholder':"Ingrese un valor",
                    'autocomplete': 'off',
                    'class':'form-control',
                     "onkeydown":"noPuntoComa( event )"
                }
            ),
            "cuotas": NumberInput(
                attrs={
                    'id':'cuotas',
                    'placeholder':"Ingrese un valor",
                    'autocomplete': 'off',
                    'class':'form-control',
                     "onkeydown":"noPuntoComa( event )"
                }
            ),
            "cuota_valor": NumberInput(
                attrs={
                    'id':'cuota_valor',
                    'placeholder':"Ingrese un valor",
                    'autocomplete': 'off',
                    'class':'form-control',
                     "onkeydown":"noPuntoComa( event )"
                }
            ),
            "derechosGrado": NumberInput(
                attrs={
                    'id':'derechosGrado',
                    'placeholder':"Ingrese un valor",
                    'autocomplete': 'off',
                    'class':'form-control',
                     "onkeydown":"noPuntoComa( event )"
                }
            ),
            'costo': HiddenInput(
                attrs={
                    'id':'costo'
                }
            ),
             'tipe': Select(
                attrs={
                    'id':'tipe',
                    'class':'form-control'
                }
            ),


        }

    
    
    def clean_programa_name(self):

        nombre = str(self.cleaned_data.get('programa_name'))

        return nombre.title()
    


##Formulario de asignaturas
class InventarioRegisterForm(forms.ModelForm):

    class Meta:
        model = Inventario
        fields = ('__all__')
        exclude =['an_creacion', "updated_at", "codigo"]

        widgets={

            'nombre_materia': TextInput(
                attrs={
                    'id':'nombre_materia',
                    'placeholder':"Ingrese un nombre",
                    'autocomplete': 'off',
                    'class':'form-control'
                }
            ),
            'programa': Select(
                attrs={
                    'autocomplete': 'off',
                    'class':'form-control',
                    'id': 'programa'

                }
            ),

                
        } 
    
   
##Formulario de asignaturas de manera masiva  
class InventarioMasiveForm(forms.Form):

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




##Formulario de asignaturas 
class MateriasForm(forms.ModelForm):
    
    def __init__(self,*args,**kwargs):
        super (MateriasForm,self ).__init__(*args,**kwargs)
        self.fields['docente'].queryset = Docente.objects.filter(is_active = True)
    
    
    

    class Meta:
        model = Materias
        fields = ('__all__')
        exclude =['an_creacion', 'is_active', 'updated_at']

        widgets={


                'materia': HiddenInput(
                    attrs={
                        'id': 'materia'

                    }
                ),
                'sede': Select(
                    attrs={
                        'autocomplete': 'off',
                        'class':'form-control',
                        'id': 'sede'

                    }
                ),

                'periodo': Select(
                    attrs={
                        'autocomplete': 'off',
                        'class':'form-control',
                        'id': 'periodo'
                    }
                ),
                'jornada': Select(
                    attrs={
                        'autocomplete': 'off',
                        'class':'form-control',
                        'id': 'jornada'
                    }
                ),
                'docente': Select(
                    
                    attrs={
                        'autocomplete': 'off',
                        'class':'form-control',
                        "id":"docente"
                    }
                ),
                "pre_cierre":DateInput(
                    format=('%Y-%m-%d'),
                    attrs={
                        "type": "date", 
                        "class": "form-control",
                        "id":"pre_cierre"
                    },
                ),
                "cierre":DateInput(
                    format=('%Y-%m-%d'),
                    attrs={
                        "type": "date", 
                        "class": "form-control",
                        "id":"cierre"
                    },
                ),
        }


##Formulario de asignacion de tareas en Banner
        
class BannerTaksForm(forms.ModelForm):

    class Meta:
        model = Banner
        fields = ('__all__')
        exclude =['student', "cod_tarea", "calificacion"]

        widgets={


                'materia':  HiddenInput(
                    attrs={
                        'id': 'materia'

                    }
                ),
                'tarea': Select(
                    attrs={
                        'autocomplete': 'off',
                        'class':'form-control',
                        'id': 'tarea'

                    }
                ),
                "observacion":Textarea(
                attrs={
                    'autocomplete': 'off',
                    'class':'form-control ',
                    'id': 'observacion'
                }
            ),
        }

    def clean_tarea(self):
        tarea = str(self.cleaned_data.get("tarea"))
        if tarea == "Sin asignar":
            raise forms.ValidationError("Debes seleccionar una actividad diferente a 'Sin asignar'.")
        return self.cleaned_data.get("tarea")
    

##Formulario de eliminacion de tareas en Banner
        
class BannerTaksDeleteForm(forms.ModelForm):

    class Meta:
        model = Banner
        fields = ('__all__')
        exclude =['student', "cod_tarea", "calificacion",'tarea',"observacion"]

        widgets={


                'cod_tarea':  HiddenInput(
                    attrs={
                        'id': 'cod_tarea'

                    }
                ),
        }


#Formulario de cargue masivo de estudiantes.
class BannerFormCharge(forms.Form):

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

        if carga_file1 != 'cargue_notas.xlsx' :
           self.add_error('carga', 'Archivo inválido, recuerde que el archivo tiene por nombre "cargue_notas.xlsx" , por favor verifique y cárguelo nuevamente')

        else:
            return carga_file_exp
        