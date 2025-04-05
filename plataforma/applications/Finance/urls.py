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
        'finance-create-other-incomes/<pk>/',
        views.FinanceOtherIncomesCreateview.as_view(),
        name='finance-create-other-incomes'
    ),

    path(
        'finance-list-student-invoice/<slug:slug>/',
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
    
    path(
        'finance-list-nominas/<pk>/',
        views.FinanceNominaListUserView.as_view(),
        name='finance-list-nominas'
    ),
    path(
        'finance-create-nominas/<pk>/',
        views.FinanceNominaView.as_view(),
        name='finance-create-nominas'
    ),
    path(
        'finance-detail-nominas/<pk>/',
        views.FinanceNominaDetailView.as_view(),
        name='finance-detail-nominas'
    ),

    path(
        'finance-delete-nominas/<pk>/',
        views.FinanceNominaDeleteView.as_view(),
        name='finance-delete-nominas'
    ),
    path(
        'finance-generate-nominas/<pk>/',
        views.GenerarNominaView.as_view(),
        name='finance-generate-nominas'
    ),
    path(
        'finance-generate-recibos/<pk>/',
        views.GenerarReciboView.as_view(),
        name='finance-generate-recibos'
    ),
    path(
        'download-report-daily/',
        views.GenerarInformeDiarioDiaView.as_view(),
        name='download-report-daily'
    ),

    path(
        'download-report-init/',
        views.FinanceInformeTemplateView.as_view(),
        name='download-report-init'
    ),

    path(
        'download-report-rango/',
        views.GenerarInformeDiarioRangoView.as_view(),
        name='download-report-rango'
    ),

    path(
        'finance-list-my-pays/',
        views.FinanceInvoiceMyPayListview.as_view(),
        name='finance-list-my-pays'
    ),
    


    

    

    

    


    
]


