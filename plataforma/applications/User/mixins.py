from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse

class AdminRequiredMixin(LoginRequiredMixin):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse('homepage_app:login'))  
        
        if not (self.is_admin(request.user) or self.is_gestor(request.user)):
            logout(request)  
            previous_url = reverse('homepage_app:logout')
            return redirect(previous_url)
        
        return super().dispatch(request, *args, **kwargs)

    def is_admin(self, user):
        return user.tipe.rol == "Administrador"

    def is_gestor(self, user):
        return user.tipe.rol == "Gestor"

#Mixin para verificar que si sea administrador o gestor el que quiere acceder a una vista y que esté logueado
class OnlyAdminRequiredMixin(LoginRequiredMixin): 
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse('homepage_app:login'))  
        
        if not self.is_admin(request.user):
            logout(request)  
            previous_url = reverse('homepage_app:logout')
            return redirect(previous_url)
        
        return super().dispatch(request, *args, **kwargs)

    def is_admin(self, user):
        return user.tipe.rol == "Administrador"
    

class StudentRequiredMixin(LoginRequiredMixin):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse('homepage_app:login'))  
        
        if not  self.is_estudiante(request.user):
            logout(request)  
            previous_url = reverse('homepage_app:logout')
            return redirect(previous_url)
        
        return super().dispatch(request, *args, **kwargs)

    def is_estudiante(self, user):
        return user.tipe.rol == "Estudiante"
    

class TeacherRequiredMixin(LoginRequiredMixin):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse('homepage_app:login'))  
        
        if not  self.is_docente(request.user):
            logout(request)  
            previous_url = reverse('homepage_app:logout')
            return redirect(previous_url)
        
        return super().dispatch(request, *args, **kwargs)

    def is_docente(self, user):
        return user.tipe.rol == "Docente"
    
class AdminTeacherRequiredMixin(LoginRequiredMixin):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse('homepage_app:login'))  
        
        if not (self.is_admin(request.user) or self.is_docente(request.user) or self.is_gestor(request.user))  :
            logout(request)  
            previous_url = reverse('homepage_app:logout')
            return redirect(previous_url)
        
        return super().dispatch(request, *args, **kwargs)

    def is_admin(self, user):
        return user.tipe.rol == "Administrador"
    
    def is_docente(self, user):
        return user.tipe.rol == "Docente"

    def is_gestor(self, user):
        return user.tipe.rol == "Gestor"
    
class AdminCoordinadorRequiredMixin(LoginRequiredMixin):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse('homepage_app:login'))  
        
        if not (self.is_admin(request.user) or self.is_coordinador(request.user) or self.is_gestor(request.user))  :
            logout(request)  
            previous_url = reverse('homepage_app:logout')
            return redirect(previous_url)
        
        return super().dispatch(request, *args, **kwargs)

    def is_admin(self, user):
        return user.tipe.rol == "Administrador"
    
    def is_coordinador(self, user):
        return user.tipe.rol == "Coordinador"

    def is_gestor(self, user):
        return user.tipe.rol == "Gestor"
    

class CoordinatorRequiredMixin(LoginRequiredMixin):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse('homepage_app:login'))  
        
        if not  self.is_docente(request.user):
            logout(request)  
            previous_url = reverse('homepage_app:logout')
            return redirect(previous_url)
        
        return super().dispatch(request, *args, **kwargs)

    def is_docente(self, user):
        return user.tipe.rol == "Coordinador"