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
]


