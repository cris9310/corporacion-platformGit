from django.forms import *
from django import forms
from django.contrib.auth.forms import AuthenticationForm



from .models import *





#formularios login

class UserLoginForm(AuthenticationForm):

    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(
            attrs = {
                'placeholder': 'Ingrese usuario',
                'autocomplete': 'off',
                'class':'form-control ',
            }
        )
    )

    password = forms.CharField(
        label='Contraseña', 
        widget=forms.PasswordInput(
            attrs = {
                'placeholder': 'Contraseña',
                'autocomplete': 'off',
                'class':'form-control ',
            }
        )
    )





# Formulario para la creación de usuarios

class UserRegisterForm(forms.ModelForm):


    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Contraseña',
                'class':'form-control ',
                'id':'password1'

            }
        )

    )
    password2 = forms.CharField(
        label='Confirme contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Repetir contraseña',
                'class':'form-control ',
                'id':'password2'

            }
        )

    )

    class Meta:

        model = User
        fields = ('__all__')
        exclude =['password','last_login', 'is_superuser', 'is_active','is_staff','created_at']
        
        widgets={


        'codigo' :NumberInput(
            attrs={
                'autocomplete': 'off',
                'class':'form-control ',
                 'id':'codigo'
            }
        ),
        'tipe': Select(
                attrs={
                    
                    'autocomplete': 'off',
                    'class':'form-control',
                    "id": "tipe"
                }
            ),
        'nombres' :TextInput(
            attrs={
                'placeholder':'Ingrese el nombre',
                'autocomplete': 'off',
                'class':'form-control ',
                "id": "nombres"
            }
        ),
        'apellidos' :TextInput(
            attrs={
                'placeholder':'Ingrese apellidos',
                'autocomplete': 'off',
                'class':'form-control ',
                "id": "apellidos"
            }
        ),
    

        'username' :TextInput(
            attrs={
                'placeholder':'Ingrese username',
                'autocomplete': 'off',
                'class':'form-control ',
                "id": "username"
            }
        ),
        

        'email' : EmailInput(
            
            attrs={
                'placeholder':'Ingrese email',
                'autocomplete': 'off',
                'class':'form-control ',
                "id": "email"
            }
        )
        
    }
    
    def clean_tipe(self):
        tipe = str(self.cleaned_data.get("tipe"))
        if tipe == "Estudiante" or tipe == "Docente":
            raise forms.ValidationError("En este formulario no se pueden crear perfiles para estudiantes ni docentes.")
        return self.cleaned_data.get("tipe")

             

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2
    
# Formulario para la actualizacion de usuarios
class UserUpdateForm(forms.ModelForm):


    class Meta:

        model = User
        fields = ('__all__')
        exclude =['password','last_login', 'is_superuser', 'is_active','is_staff','created_at']
        
        widgets={


        'codigo' :NumberInput(
            attrs={
                'autocomplete': 'off',
                'class':'form-control ',
                 'id':'codigo'
            }
        ),
        'tipe': Select(
                attrs={
                    
                    'autocomplete': 'off',
                    'class':'form-control',
                    "id": "tipe"
                }
            ),
        'nombres' :TextInput(
            attrs={
                'placeholder':'Ingrese el nombre',
                'autocomplete': 'off',
                'class':'form-control ',
                "id": "nombres"
            }
        ),
        'apellidos' :TextInput(
            attrs={
                'placeholder':'Ingrese apellidos',
                'autocomplete': 'off',
                'class':'form-control ',
                "id": "apellidos"
            }
        ),
    

        'username' :TextInput(
            attrs={
                'placeholder':'Ingrese username',
                'autocomplete': 'off',
                'class':'form-control ',
                "id": "username"
            }
        ),
        

        'email' : EmailInput(
            
            attrs={
                'placeholder':'Ingrese email',
                'autocomplete': 'off',
                'class':'form-control ',
                "id": "email"
            }
        )
        
    }
    
    def clean_tipe(self):
        tipe = str(self.cleaned_data.get("tipe"))
        if tipe == "Estudiante" or tipe == "Docente":
            raise forms.ValidationError("En este formulario no se pueden crear perfiles para estudiantes ni docentes.")
        return self.cleaned_data.get("tipe")

