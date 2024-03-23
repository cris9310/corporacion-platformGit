from django.urls import path
from . import views
app_name = 'homepage_app'

urlpatterns = [
   
   path(
      '',
      views.RedirectView,
   ),
   path(
      'home/',
      views.HomePageView.as_view(), 
      name='home'
   ),
   path(
      'programs/primaria/',
      views.PrimariaPageView.as_view(), 
      name='primaria'
   ),

   path(
      'programs/bachillerato/',
      views.BachilleratoPageView.as_view(), 
      name='bachillerato'
   ),

    path(
      'programs/tecnico-sistemas/',
      views.SistemasPageView.as_view(), 
      name='sistemas'
   ),

   path(
      'programs/tecnico-administracion/',
      views.AdminPageView.as_view(), 
      name='administracion'
   ),
   path(
      'programs/tecnico-primera-infancia/',
      views.PrimeraInfanciaPageView.as_view(), 
      name='primera-infancia'
   ),
   path(
      'programs/tecnico-secretariado/',
      views.SecretariadoPageView.as_view(), 
      name='secretariado'
   ),
   path(
      'programs/tecnico-general/',
      views.TecnicosGeneralPageView.as_view(), 
      name='tecnico-general'
   ),
   path(
      'programs/calendario-home/',
      views.CalendarPageView.as_view(), 
      name='calendario-home'
   ),

   path(
      'contact/',
      views.ContactView.as_view(), 
      name='contact'
   ),

   path(
      'mirando/',
      views.Error404View.as_view(), 
      name='mirando'
   ),

   

   

   
   
   path(
      'login/', 
      views.AdminLogin.as_view(),
      name="login"
   ),

   path(
      'logout/', 
      views.AdminLogout.as_view(),
      name="logout"
   )  
]

