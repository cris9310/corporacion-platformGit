from django.urls import path
from . import views
app_name = 'settings_app'

urlpatterns = [
    
    path(
        'config',
        views.ConfigTemplateView.as_view(),
        name='config'
    ),
    path(
        'create-periodo/',
        views.PeriodoCreateView.as_view(),
        name='create-periodo'
    ),
    path(
        'list-periodo/',
        views.PeriodoListView.as_view(),
        name='list-periodo'
    ),
    path(
        'delete-periodo/<pk>/',
        views.PeriodoDeleteView.as_view(),
        name='delete-periodo'
    ),


    

    path(
        'create-programas/',
        views.ProgramaCreateView.as_view(),
        name='create-programas'
    ),
    path(
        'list-program/',
        views.Programalistview.as_view(),
        name='list-program'
    ),
    path(
        'detail-program/<pk>/',
        views.ProgramaDetailView.as_view(),
        name='detail-program'
    ),
    path(
        'update-Program/<pk>/',
        views.ProgramaUpdateView.as_view(),
        name='update-Program'
    ),
    path(
        'delete-Program/<pk>/',
        views.ProgramaDeleteView.as_view(),
        name='delete-Program'
    ),
]


