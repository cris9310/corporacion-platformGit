from django.urls import path
from . import views
app_name = 'teacher_app'

urlpatterns = [
    
    path(
        'teacher-list',
        views.Teacherlistview.as_view(),
        name='teacher-list'
    ),

    path(
        'teacher-create',
        views.TeacherCreateView.as_view(),
        name='teacher-create'
    ),
    
    path(
        'teacher-update/<pk>/',
        views.TeacherUpdateView.as_view(),
        name='teacher-update'
    ),

    path(
        'teacher-detail/<pk>/',
        views.TeacherDetailView.as_view(),
        name='teacher-detail'
    ),

    path(
        'teacher-habilit/<pk>/',
        views.TeacherHabilitView.as_view(),
        name='teacher-habilit'
    ),

    path(
        'teacher-delete/<pk>/',
        views.TeacherDeleteView.as_view(),
        name='teacher-delete'
    ),

    path(
        'teacher-topic-list/<slug:slug>/',
        views.TeacherTopicsListview.as_view(),
        name='teacher-topic-list'
    ),

    

    
]


