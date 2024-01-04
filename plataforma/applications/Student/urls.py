from django.urls import path
from . import views
app_name = 'student_app'

urlpatterns = [

    
    path(
        'home-student/',
        views.StudentTemplateView.as_view(),
        name='home-student'
    ),

    path(
        'create-student/',
        views.StudentCreateView.as_view(),
        name='create-student'
    ),

    path(
        'list-top-asignar/',
        views.StudentAsigView.as_view(),
        name='list-top-asignar'
    ),
    path(
        'list-student/list-student-cargue/',
        views.StudentCargueListview.as_view(),
        name='list-student-cargue'
    ),
    path(
        'update-student/<pk>/',
        views.StudentMasiveUpdateView.as_view(),
        name='update-student'
    ),
    path(
        'export-plant-student',
        views.export_users_csv,
        name='export-plant-student'
    ),
    path(
        'delete-student-finally/<pk>/',
        views.StudentDeleteView.as_view(),
        name='delete-student-finally'
    ),
    path(
        'detail-student/<pk>/',
        views.StudentDetailView.as_view(),
        name='detail-student'
    ),
    path(
        'list-student/',
        views.Studentlistview.as_view(),
        name='list-student'
    ),
    

    
]


