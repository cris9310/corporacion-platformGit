from django.forms import *
from django import forms

from .models import *


class PeriodoForm(forms.Form):

    Año = forms.CharField(
        label='Año',
        required=True,
        widget=forms.NumberInput()

    )

    periodo = forms.CharField(
        label='periodo',
        required=True,
        widget=forms.NumberInput()

    )

    def clean_periodo(self):
        ano = self.cleaned_data.get('Año')
        periodo = self.cleaned_data.get('periodo')
        concat=str(ano) + "-" + periodo
        
        if Periodos.objects.filter(periodo = concat).exists() :
           self.add_error('Año', 'El periodo que intenta crear ya existe.')
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
                    'placeholder':"Ingrese un nombre",
                    'autocomplete': 'off',
                    'class':'form-control'
                }
            ),
            'costo': HiddenInput(),
             'tipe': Select(
                attrs={
                    'id':'Tipo_program',
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
