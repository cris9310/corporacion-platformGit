from django.shortcuts import redirect
from django.urls import reverse


from datetime import timedelta

class RoleBasedSessionTimeoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        
        if request.user.is_authenticated:
            if request.user.tipe.rol == 'Administrador' or request.user.tipe.rol == 'Gestor': 
                request.session.set_expiry(timedelta(minutes=30).total_seconds())
            elif request.user.tipe.rol == 'Coordinador' or request.user.tipe.rol == 'Docente':
                request.session.set_expiry(timedelta(minutes=40).total_seconds())
            else:
                request.session.set_expiry(timedelta(minutes=60).total_seconds())
        return response
    


class ForcePasswordChangeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and request.user.cambiar_contrasena:
            if request.path not in [reverse('user_app:CambiarPassword'), reverse('homepage_app:logout')]:
                return redirect('user_app:CambiarPassword')
        return self.get_response(request)
    


class DisableCacheMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.user.is_authenticated:
            return response
        response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        response['Pragma'] = 'no-cache'
        response['Expires'] = '0'
        return response