"""
URL configuration for plataforma project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404


from applications.Homepage.views import Error404View

urlpatterns = [

    path('admin/', admin.site.urls),

    path('', include('applications.Homepage.urls')),
    path('user/', include('applications.User.urls')),
    path('settings/', include('applications.Programs.urls')),
    path('student/', include('applications.Student.urls')),
    path('teacher/', include('applications.Teacher.urls')),

    #path('agenda/', include('applications.Agenda.urls')),
    path('finance/', include('applications.Finance.urls')),
    path('dashboard/', include('applications.Dashboard.urls')),


]

handler404 = Error404View.as_view()


