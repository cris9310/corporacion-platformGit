from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse

#Mixin para verificar que si sea administrador el que quiere acceder a una vista y que esté logueado
class AdminRequiredMixin(LoginRequiredMixin): 
    def dispatch(self, request, *args, **kwargs):
       
        if not request.user.is_authenticated  or not self.is_admin(request.user):
            if not request.user.is_authenticated:
                previous_url = reverse('homepage_app:login')
                return redirect(previous_url)  # Si no está autenticado, redirige al inicio de sesión
            elif not self.is_admin(request.user):
                logout(request)
                previous_url = reverse('homepage_app:logout')
                return redirect(previous_url)
        return super().dispatch(request, *args, **kwargs)
    
    def is_admin(self, user):
        return user.tipe.rol == "Administrador"
    
class AdminTeacherRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
       
        if not request.user.is_authenticated  or not self.is_admin(request.user) or not self.is_teacher(request.user):
            if not request.user.is_authenticated:
                previous_url = reverse('homepage_app:login')
                return redirect(previous_url)  # Si no está autenticado, redirige al inicio de sesión
            elif not self.is_admin(request.user):
                logout(request)
                previous_url = reverse('homepage_app:logout')
                return redirect(previous_url)
            elif not self.is_teacher(request.user):
                logout(request)
                previous_url = reverse('homepage_app:logout')
                return redirect(previous_url)
        return super().dispatch(request, *args, **kwargs)
    
    def is_admin(self, user):
        return user.tipe.rol == "Administrador"
    def is_teacher(self, user):
        return user.tipe.rol == "Docente"