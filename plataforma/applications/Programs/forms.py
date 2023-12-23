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
    

class MateriasForm(forms.ModelForm):
    
    def __init__(self,*args,**kwargs):
        super (MateriasForm,self ).__init__(*args,**kwargs)
        self.fields['docente'].queryset = Docente.objects.filter(is_active = True)
    
    
    

    class Meta:
        model = Materias
        fields = ('__all__')
        exclude =['an_creacion', 'is_active', 'codigo']

        widgets={

                'materia': Select(
                    attrs={
                        'autocomplete': 'off',
                        'class':'form-select ',
                        'id': 'materia'

                    }
                ),
                'programa': Select(
                    attrs={
                        'autocomplete': 'off',
                        'class':'form-select ',
                        'id': 'carrera'

                    }
                ),
                'sede': Select(
                    attrs={
                        'autocomplete': 'off',
                        'class':'form-select ',
                        'id': 'sede'

                    }
                ),
                'pensum_asig': Select(
                    attrs={
                        'class':'form-select ',
                        'id': 'pensum_asig'

                    }
                ),

                'periodo': Select(
                    attrs={
                        'autocomplete': 'off',
                        'class':'form-select '
                    }
                ),
                'docente': Select(
                    
                    attrs={
                        'autocomplete': 'off',
                        'class':'form-select '
                    }
                ),
                
        }

    

    def clean_codigo(self):
        b = (self.cleaned_data.get('codigo'))
        if b[0] == "0":
            self.add_error('codigo', 'El código no puede iniciar por cero')
        else:
            return b
        
    
class InventarioRegisterForm(forms.ModelForm):

    class Meta:
        model = Inventario
        fields = ('__all__')
        exclude =['an_creacion']

        widgets={

                'programa': Select(
                    attrs={
                        'autocomplete': 'off',
                        'class':'form-select ',
                        'id': 'carrera'

                    }
                ),

                'pensum_asig_inv': Select(
                    attrs={
                        'autocomplete': 'off',
                        'class':'form-select ',
                        'id': 'pensum_asig'

                    }
                ),
                
                
        } 
