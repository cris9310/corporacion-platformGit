from django.shortcuts import HttpResponseRedirect
from django.views.generic import TemplateView, FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.conf import settings
from django.core.mail import send_mail


from .forms import *
from applications.User.forms import UserLoginForm


def RedirectView(request):

    return HttpResponseRedirect(
        reverse_lazy('homepage_app:home')
        )

class HomePageView(TemplateView):
    template_name = "homepage/homepageContent.html"

class PrimariaPageView(TemplateView):
    template_name = "homepage/programPrimaria.html"

class BachilleratoPageView(TemplateView):
    template_name = "homepage/programBachillerato.html"

class SistemasPageView(TemplateView):
    template_name = "homepage/programSistemas.html"

class AdminPageView(TemplateView):
    template_name = "homepage/programAdmin.html"

class PrimeraInfanciaPageView(TemplateView):
    template_name = "homepage/programPrimeraInfancia.html"

class SecretariadoPageView(TemplateView):
    template_name = "homepage/programSecretariado.html"

class TecnicosGeneralPageView(TemplateView):
    template_name = "homepage/programsTecnicosGeneral.html"

class CalendarPageView(TemplateView):
    template_name = "homepage/calendarhome.html"


class ContactView(FormView):
    form_class = ContactForm
    template_name = "homepage/contact.html"
    success_url = reverse_lazy('homepage_app:contact')


    def post(self, request, *args, **kwargs):

        form = ContactForm(self.request.POST) 
        if form.is_valid():

            nombre=form.cleaned_data.get("nombre")
            apellidos=form.cleaned_data.get("apellidos")
            email=form.cleaned_data.get("email")
            telefono=form.cleaned_data.get("telefono")
            observacion=form.cleaned_data.get("observacion")
            


            full_message = f"""
            Hemos recibido un nuevo mensaje de  {nombre} {apellidos}, con email: {email}. Número de contacto: {telefono}
            ________________________

            
            {observacion}
            """
            send_mail(
            subject="Solicitud de contacto --- pagina web",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.NOTIFY_EMAIL],
        )
            mensaje = f'Datos registrados correctamente'
            error = "No hay error!"
            response = JsonResponse({"mensaje": mensaje, "error": error})
            response.status_code = 201
            return response
        else:
            mensaje=[]
            mensaje.append({"error": "Formulario incompleto, por favor valide."})
            response = JsonResponse(mensaje, safe=False)
            response.status_code = 400
            return response






class Error404View(TemplateView):
    template_name = "homepage/Error404.html"

class AdminLogin(LoginView):
    template_name = 'homepage/LoginView_form.html'
    form_class = UserLoginForm

class AdminLogout(LogoutView):
    template_name = 'homepage/Logout.html'