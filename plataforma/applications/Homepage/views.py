from django.shortcuts import HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy


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


    

class AdminLogin(LoginView):
    template_name = 'homepage/LoginView_form.html'

class AdminLogout(LogoutView):
    template_name = 'homepage/Logout.html'