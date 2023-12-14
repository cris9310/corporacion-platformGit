from django.shortcuts import HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy


def RedirectView(request):

    return HttpResponseRedirect(
        reverse_lazy('homepage_app:home')
        )

class HomePageView(TemplateView):
    template_name = "homepage/homepage.html"

class AdminLogin(LoginView):
    template_name = 'homepage/LoginView_form.html'

class AdminLogout(LogoutView):
    template_name = 'homepage/Logout.html'