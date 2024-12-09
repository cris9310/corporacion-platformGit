from django.forms import *
from django import forms


from .models import *


#Formulario destinado a la creación de gastos, está ok
class SpendForm(forms.ModelForm):


    class Meta:

        model = Gastos
        fields = ('__all__')
        exclude =['codigo']

        widgets={

            'tipo': Select(
                attrs={
                    'class':'form-control',
                    'id': 'tipo',
                    "onchange":"handleChange(this)"
                }
            ),
            'consecutivo': NumberInput(
                attrs={
                    'type':'number',
                    'class':'form-control',
                    'id': 'consecutivo',
                    "onkeydown":"noPuntoComa( event )"
                }
            ),
            
            'descripcion': TextInput(
                attrs={
                    'placeholder':"Ingrese las descripción",
                    'autocomplete': 'off',
                    'class':'form-control',
                    'id': 'descripcion'
                }
            ),
            "fecha":DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    "type": "date", 
                    "class": "form-control",
                    "id":"fecha"
                },
            ),
            'monto': NumberInput(
                attrs={
                    'type':'number',
                    'class':'form-control',
                    'id': 'monto',
                    "onkeydown":"noPuntoComa( event )"
                }
            ),

        }
    
    def clean_consecutivo(self):
        if FacturasSub.objects.filter(
            consecutivo=self.cleaned_data.get('consecutivo')
            ) or Gastos.objects.filter(
                consecutivo=self.cleaned_data.get('consecutivo')) or OtroIngreso.objects.filter(
                consecutivo=self.cleaned_data.get('consecutivo')):
           
           self.add_error('consecutivo', 'Este consecutivo ya existe, por favor verifique.')
        else:
           return self.cleaned_data.get('consecutivo')


#Formulario destinado a la creación de otros ingresos, está ok
class OtherIncomesForm(forms.ModelForm):


    class Meta:

        model = OtroIngreso
        fields = ('__all__')
        exclude =['codigo']

        widgets={

            'consecutivo': NumberInput(
                attrs={
                    'type':'number',
                    'class':'form-control',
                    'id': 'consecutivo',
                    "onkeydown":"noPuntoComa( event )"
                }
            ),
            'tipo': Select(
                attrs={
                    'class':'form-control',
                    'id': 'tipo',
                    "onchange":"handleChange(this)"
                }
            ),
            'descripcion': TextInput(
                attrs={
                    'placeholder':"Ingrese las descripción",
                    'autocomplete': 'off',
                    'class':'form-control',
                    'id': 'descripcion'
                }
            ),
            "fecha":DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    "type": "date", 
                    "class": "form-control",
                    "id":"fecha"
                },
            ),
            'monto': NumberInput(
                attrs={
                    'type':'number',
                    'class':'form-control',
                    'id': 'monto',
                    "onkeydown":"noPuntoComa( event )"
                }
            ),

        }
    
    def clean_consecutivo(self):
        if FacturasSub.objects.filter(
            consecutivo=self.cleaned_data.get('consecutivo')
            ) or Gastos.objects.filter(
                consecutivo=self.cleaned_data.get('consecutivo')) or OtroIngreso.objects.filter(
                consecutivo=self.cleaned_data.get('consecutivo')):
           
           self.add_error('consecutivo', 'Este consecutivo ya existe, por favor verifique.')
        else:
           return self.cleaned_data.get('consecutivo')
        


#Formulario que actualiza las facturas de los estudiantes

class FacturasForm(forms.ModelForm):
    
    class Meta:

        model = FacturasSub
        fields = ['consecutivo', 'pagado','observacion' ]
        # campos requeridos 
        widgets = {

            "pagado": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "id": "pagado",
                    'placeholder':"Ingrese el valor pagado",
                    "onkeydown":"noPuntoComa( event )"
                }
            ),
            "observacion": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id":"observacion",
                    'autocomplete': 'off',
                }
            ),
            'consecutivo': forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "id": "consecutivo",
                    'placeholder':"Ingrese el consecutivo",
                    "onkeydown":"noPuntoComa( event )"
                }
            ),
        }
    
    def __init__(self, *args, **kwargs):
        super(FacturasForm, self).__init__(*args, **kwargs)
        self.fields['observacion'].label = "Observación"
        self.fields['pagado'].label = "Valor a pagar"

    def clean_consecutivo(self):
        if FacturasSub.objects.filter(
            consecutivo=self.cleaned_data.get('consecutivo')
            ) or Gastos.objects.filter(
                consecutivo=self.cleaned_data.get('consecutivo')) or OtroIngreso.objects.filter(
                consecutivo=self.cleaned_data.get('consecutivo')):
           
           self.add_error('consecutivo', 'Este consecutivo ya existe, por favor verifique.')
        else:
           return self.cleaned_data.get('consecutivo')