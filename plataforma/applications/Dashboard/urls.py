from django.urls import path
from . import views
app_name = 'dashboard_app'

urlpatterns = [
    
    path(
        'dashboard-admin',
        views.DashboardAdminView.as_view(),
        name='dashboard-admin'
    ),
    path(
        'dashboard-user',
        views.RedirectUserView,
        name='dashboard-user'
    ),
    
]


