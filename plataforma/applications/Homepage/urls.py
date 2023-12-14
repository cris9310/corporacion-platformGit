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

