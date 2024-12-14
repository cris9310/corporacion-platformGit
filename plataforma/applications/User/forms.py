from django.forms import *
from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.password_validation import validate_password



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


class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contraseña actual'
        }),
        label="Contraseña actual"
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nueva contraseña'
        }),
        label="Nueva contraseña"
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirmar nueva contraseña'
        }),
        label="Confirmar nueva contraseña"
    )

    def clean_old_password(self):

        old_password = self.cleaned_data.get('old_password')
        if not self.user.check_password(old_password):
            raise forms.ValidationError("La contraseña ingresada no es correcta.")
        return old_password
    
    def clean_new_password1(self):
        new_password = self.cleaned_data.get('new_password1')
        validate_password(new_password, self.user)
        return new_password

    def clean(self):

        cleaned_data = super().clean()
        new_password1 = cleaned_data.get('new_password1')
        new_password2 = cleaned_data.get('new_password2')

        if new_password1 and new_password2:
            if new_password1 != new_password2:
                raise forms.ValidationError("Las nuevas contraseñas no coinciden.")
            if self.user.check_password(new_password1):
                raise forms.ValidationError("La nueva contraseña no puede ser igual a la contraseña actual.")

        return cleaned_data