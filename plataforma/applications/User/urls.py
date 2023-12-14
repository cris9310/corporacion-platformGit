from django.urls import path
from . import views
app_name = 'user_app'

urlpatterns = [
    path(
        'create-user/',
        views.UserCreateView.as_view(),
        name='create-user'
    ),
    path(
        'list-user/',
        views.UserListView.as_view(),
        name='list-user'
    ),
    path(
        'detail-user/<pk>/',
        views.UserDetailView.as_view(),
        name='detail-user'
    ),

    path(
        'update-user/<pk>/',
        views.UserUpdateView.as_view(),
        name='update-user'
    ),
    path(
        'deleted-user/<pk>/',
        views.UserDeleteView.as_view(),
        name='deleted-user'
    ),

    path(
        'enable-user/<pk>/',
        views.UserEnableView.as_view(),
        name='enable-user'
    ),

    path(
        'profile/',
        views.UserProfileDetailView.as_view(),
        name='profile'
    ),
]
