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
        'config/list-periodo/',
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
        'config/list-program/',
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





    path(
        'config/list-inventario/',
        views.Inventariolistview.as_view(),
        name='list-inventario'
    ),
    path(
        'create-inventario/',
        views.InventarioCreateView.as_view(),
        name='create-inventario'
    ),
    path(
        'update-inventario/<pk>/',
        views.InventarioUpdateView.as_view(),
        name='update-inventario'
    ),

    path(
        'delete-inventario/<pk>/',
        views.InventarioDeleteView.as_view(),
        name='delete-inventario'
    ),
    path(
        'export-plant-asignaturas',
        views.InventarioMasiveExport,
        name='export-plant-asignaturas'
    ),
    path(
        'create-masive-asignaturas/',
        views.InventarioMasiveView.as_view(),
        name='create-masive-asignaturas'
    ),





    path(
        'create-materias/<pk>/',
        views.MateriasCreateView.as_view(),
        name='create-materias'
    ),
    path(
        'list-materias/<pk>/',
        views.Materialistview.as_view(),
        name='list-materias'
    ),

    path(
        'create-banner/',
        views.BannerCreateView.as_view(),
        name='create-banner'
    ),
    

    



    




    



    
]


