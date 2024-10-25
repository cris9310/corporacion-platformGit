from django.urls import path
from . import views
app_name = 'finance_app'

urlpatterns = [
    
    path(
        'finance-general-list-view',
        views.FinanceGeneralListView.as_view(),
        name='finance-general-list-view'
    ),

    path(
        'finance-create-spend',
        views.FinanceSpendCreateview.as_view(),
        name='finance-create-spend'
    ),

    path(
        'finance-create-other-incomes',
        views.FinanceOtherIncomesCreateview.as_view(),
        name='finance-create-other-incomes'
    ),

    path(
        'finance-list-student-invoice/<pk>/',
        views.FinanceInvoiceListviewStudent.as_view(),
        name='finance-list-student-invoice'
    ),
 
    path(
        'finance-update-student-invoice/<pk>/',
        views.FinanceInvoiceUpdateStudent.as_view(),
        name='finance-update-student-invoice'
    ),

    path(
        'finance-update-student-invoice/<pk>/',
        views.FinanceInvoiceUpdateStudent.as_view(),
        name='finance-update-student-invoice'
    ),
    path(
        'detail-sub/<pk>/',
        views.FinanceFacturasSubDetailView.as_view(),
        name='detail-sub'
    ),
    path(
        'delete-sub/<pk>/',
        views.FinanceFacturasSubDeleteView.as_view(),
        name='delete-sub'
    ),
    path(
        'detail-filter-sub/',
        views.FinanceFacturasSubFilterDetailView.as_view(),
        name='detail-filter-sub'
    ),

    path(
        'download-report/',
        views.FinanceAcademicInformeView.as_view(),
        name='download-report'
    ),

    


    
]


