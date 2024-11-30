from django.db.models import Sum, Avg
from django.urls import reverse_lazy
from django.views.generic import (TemplateView,
                                  FormView, CreateView, DeleteView, UpdateView,
                                  DetailView, ListView, View)
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse


from applications.Student.models import *
from applications.Programs.models import *
from .models import *
from .forms import *


import pandas as pd
from openpyxl import Workbook
from openpyxl.writer.excel import save_virtual_workbook

#Vista para crear gastos

class FinanceSpendCreateview(CreateView):
    model = Gastos
    form_class = SpendForm
    template_name = 'finance/create_spend.html'
    success_url = reverse_lazy('finance_app:finance-general-list-view')

    def post(self, request, *args, **kwargs):

        formulario = SpendForm(self.request.POST)
        if formulario.is_valid():
            formulario.save()
            mensaje = f'{self.model.__name__} registrado correctamente'
            error = "No hay error!"
            response = JsonResponse({"mensaje": mensaje, "error": error})
            response.status_code = 201
            return response
        else:
            mensaje1 =[]
            mensaje1.append(
                {"error": formulario.errors}
            )
            response = JsonResponse(mensaje1, safe=False)
            response.status_code = 400
            return response
        

#vista para crear otros ingresos

class FinanceOtherIncomesCreateview(CreateView):
    model = OtroIngreso
    form_class = OtherIncomesForm
    template_name = 'finance/create_OtherIncomes.html'
    success_url = reverse_lazy('finance_app:finance-general-list-view')

    def post(self, request, *args, **kwargs):

        formulario = OtherIncomesForm(self.request.POST)
        if formulario.is_valid():
            formulario.save()
            mensaje = f'{self.model.__name__} registrado correctamente'
            error = "No hay error!"
            response = JsonResponse({"mensaje": mensaje, "error": error})
            response.status_code = 201
            return response
        else:
            mensaje1 =[]
            mensaje1.append(
                {"error": formulario.errors}
            )
            response = JsonResponse(mensaje1, safe=False)
            response.status_code = 400
            return response
        
#vista para registrar los pagos de mensualidades de los estudiantes
class FinanceInvoiceUpdateStudent(CreateView):
    template_name = 'finance/update_invoice.html'
    model = Facturas
    form_class = FacturasForm

    def get_context_data(self, **kwargs):
        context = super(FinanceInvoiceUpdateStudent, self).get_context_data(**kwargs)
        pagado = FacturasSub.objects.filter(
            facturas_id=self.kwargs['pk']).aggregate(pagados=Sum("pagado"))
        data = Facturas.objects.get(pk=self.kwargs['pk'])
        monto = data.monto
        pagado2 = pagado['pagados']
        pendiente = Facturas.objects.manejo(data, pagado2)
        datos = []
        info = {'pk':self.kwargs['pk'], "codigo": data.codigo, "monto": f'$ {monto:,.2f}', 'pagado': f'$ {pagado2 if pagado2 else 0.0 :,.2f}',
                'pendiente': f'$ {pendiente:,.2f}', 'pendiente2': pendiente}
        datos.append(info)
        context["datos"] = datos
        return context
    
    def post(self, request, *args, **kwargs):

        #Obtenemos las variables del formulario
        mensaje1 = []
        pendiente = self.request.POST.get('pendiente')
        facturas = self.request.POST.get('facturas')
        observacion = self.request.POST.get('observacion')
        consecutivo = self.request.POST.get('consecutivo')
        pagado = self.request.POST.get('pagado')
        characters = ",0"
        pendiente = ''.join(x for x in pendiente if x not in characters)
        formulario = FacturasForm(self.request.POST)

        if formulario.is_valid():
            #Creamos la factura relacionada a la factura principal
            matricula = FacturasSub.objects.create(
                facturas=Facturas.objects.get(codigo=facturas),
                observacion=observacion,
                consecutivo=consecutivo,
                pagado=pagado,
            )
            fact_act = FacturasSub.objects.filter(facturas_id=Facturas.objects.get(
                codigo=facturas).id).aggregate(Sum('pagado'))
            monto = Facturas.objects.get(codigo=facturas).monto
            if int(fact_act['pagado__sum']) == int(monto):
                Facturas.objects.filter(codigo=facturas).update(
                    estado_id=CatalogsTypesInvoices.objects.get(estado="Pagada"))
            elif int(fact_act['pagado__sum']) > 0 and int(fact_act['pagado__sum']) < int(monto):
                Facturas.objects.filter(codigo=facturas).update(
                    estado_id=CatalogsTypesInvoices.objects.get(estado="Abono"))
            else:
                Facturas.objects.filter(codigo=facturas).update(
                    estado_id=CatalogsTypesInvoices.objects.get(estado="Pendiente"))
                
            mensaje = f'{self.model.__name__} registrado correctamente'
            error = "No hay error!"
            response = JsonResponse({"mensaje": mensaje, "error": error})
            response.status_code = 201
            return response
        else:
            mensaje1 =[]
            mensaje1.append(
                {"error": formulario.errors}
            )
            response = JsonResponse(mensaje1, safe=False)
            response.status_code = 400
            return response




#vista para listar las facturas de los estudiantes, pendientes, abonadas y pagadas.

class FinanceInvoiceListviewStudent(ListView):
    model = Facturas
    template_name = 'finance/list_invoices.html'
    context_object_name = 'invoice'

    def get_context_data(self, **kwargs):
        context = super(FinanceInvoiceListviewStudent, self).get_context_data(**kwargs)
        context["datos"] = Estudiante.objects.get(slug=self.kwargs['slug'])
        context['progreso'] = int(int(Facturas.objects.filter(user_id=Estudiante.objects.get(slug=self.kwargs['slug']).codigo, estado_id=3).count())/int(Programas.objects.get(
            id=Estudiante.objects.get(slug=self.kwargs['slug']).carrera_id
        ).cuotas+2)*100)
        return context

    def get_queryset(self):
        info = []
        datos = Facturas.objects.filter(user_id=Estudiante.objects.get(
            slug=self.kwargs['slug']).codigo).order_by("codigo")
        
        fecha_hoy = timezone.now()
        
        for i in datos:
            pagado = FacturasSub.objects.filter(
                facturas_id=i.pk).aggregate(pagados=Sum("pagado"))
            data = pagado['pagados'] if pagado['pagados'] is not None else 0
            
           
            datos_final = {'pk': i.pk, 'slug':self.kwargs['slug'], "codigo": i.codigo, 'descripcion': i.descripcion, "fecha": i.due_at,
                        'estado': "Vencida" if i.due_at < fecha_hoy and (data < i.monto or data == 0) else i.estado, 
                        'monto': f'$ {i.monto:,.0f}', 'pagado': f'$ {data if data else 0.0 :,.0f}'}

            info.append(datos_final)

        return info

#Vista para generar informes diarios y por fechas


#vista para listar ingresos, gastos y otros ingresos
class FinanceGeneralListView(ListView):
    model = FacturasSub
    template_name = 'finance/list_income.html'
    context_object_name = 'income'
    ordering =  ['-fecha','-consecutivo'  ]

    def get_queryset(self):

        data = []
        income = FacturasSub.objects.all()
        if income:
            for i in income:
                data_json = {
                    "factor":"Ingreso","codigo":i.facturas.codigo, "consecutivo": i.consecutivo, 
                    "monto": f'$ {i.pagado if i.pagado else 0.0 :,.2f}', "fecha": i.created_at, "tipo": i.facturas.descripcion
                }
                data.append(data_json)
        
        spend = Gastos.objects.all()
        if spend:
            for i in spend:
                data_json = {
                    "factor":"Gasto","codigo":i.codigo, "consecutivo": i.consecutivo, 
                    "monto": f'$ {i.monto if i.monto else 0.0 :,.2f}', "fecha": i.fecha, "tipo": i.tipo
                }
                data.append(data_json)
        
        others_income = OtroIngreso.objects.all()
        if others_income:
            for i in others_income:
                data_json = {
                    "factor":"Ingreso","codigo":i.codigo, "consecutivo": i.consecutivo, 
                    "monto": f'$ {i.monto if i.monto else 0.0 :,.2f}', "fecha": i.fecha, "tipo": i.tipo
                }
                data.append(data_json)


        return data



#Listar las facturas sub teniendo en cuenta o filtrando en el id
class FinanceFacturasSubFilterDetailView(View):

    def get(self, request, *args, **kwargs):
        info = []
        pagados_data = FacturasSub.objects.filter(
            facturas_id=Facturas.objects.get(id=int(self.request.GET.get('info'))))

        for e in pagados_data:
            datos = {"pk": e.id, 'consecutivo': e.consecutivo, 'observacion': e.observacion, 'payed': f'$ {e.pagado:,.2f}', 'fecha': str(
                e.created_at.day) + "-" + str(e.created_at.month) + "-" + str(e.created_at.year)}
            info.append(datos)
        response = {}
        response['data'] = info
        return JsonResponse(response)


#Detalle de las facturas sub
class FinanceFacturasSubDetailView(DetailView):
    template_name = 'finance/DetailSub.html'
    model = FacturasSub


#Eliminar las facturassub
class FinanceFacturasSubDeleteView(DeleteView):
    template_name = 'finance/DeleteFactSub.html'
    model = FacturasSub
    
    
    def post(self, request, *args, **kwargs):

        data_delete = self.kwargs['pk']

        restar = FacturasSub.objects.get(id=data_delete).pagado
        facturas = FacturasSub.objects.get(id=data_delete).facturas_id
        fact_act = FacturasSub.objects.filter(
            facturas_id=facturas).aggregate(Sum('pagado'))
        fact_act = float(fact_act['pagado__sum']) - float(restar)

        #Monto original de la factura
        monto = Facturas.objects.get(id=facturas).monto
        Fac_delete = FacturasSub.objects.filter(id=data_delete).delete()
        
        #verificamos que tengamos valores consignados y que no esté vencida la factura
        if fact_act > 0 and fact_act < float(monto):
            Facturas.objects.filter(id=facturas).update(
                estado_id=CatalogsTypesInvoices.objects.get(estado="Abono"))
        else:
            Facturas.objects.filter(id=facturas).update(
                estado_id=CatalogsTypesInvoices.objects.get(estado="Pendiente"))
        return HttpResponseRedirect(
            self.request.META.get("HTTP_REFERER")
        )



#Genera informe de los estudiantes candidatos a grado
class FinanceAcademicInformeView(View):

    def post(self, request, *args, **kwargs):

        #Capturamos los valores que vienen del formulario
        estudiantes = str(self.request.POST.get('concat2'))
        select = self.request.POST.get('informe12')
        estudiantes = estudiantes.split(sep=",")
        listaDataAcademic = []
        listaDataFinance = []


        #iteramos sobre las notas y las facturas de los estudiantes que solicita el usuario
        for i in estudiantes:
            infoAcademic =Banner.objects.filter(student_id=i).values(
                "student_id", "student__nombre", "student__apellidos",
                "student__codigo",'materia__materia__nombre_materia').annotate(
                    promedio_calificacion=Avg('calificacion'))
            infoFinance = Facturas.objects.filter(
                user_id=Estudiante.objects.get(id=i).codigo)

            for j in infoAcademic:
                dataAcademic = {
                    "Codigo": j['student__codigo'], "Nombre": j['student__nombre'] + " " +
                    j['student__apellidos'], "Tipo": "Académico",
                    "Materia": j['materia__materia__nombre_materia'], "Promedio": float(j['promedio_calificacion'])
                }
                listaDataAcademic.append(dataAcademic)

            for l in infoFinance:
                dataFinance = {
                    "Codigo": l.user.codigo, "Nombre": l.user.nombres + " " +
                    l.user.apellidos, "Tipo": "Financiero",
                    "Factura": l.codigo, "Estado": l.estado.estado
                }
                listaDataFinance.append(dataFinance)

        #mandamos todo a dataframe para su posterior creacion en el excel
        dfAcademic = pd.DataFrame(listaDataAcademic)
        dfFinance = pd.DataFrame(listaDataFinance)

        # Creacion del archivo
        if select == "1":  # informe Academico
            wb = Workbook()
            ws = wb.create_sheet(index=0, title="Academico")

            headsList = list(dfAcademic.columns.values)

            for number in range(0, len(headsList)):
                Heads = ws.cell(row=1, column=number + 1)
                Heads.value = headsList[number]

            var_est = 2
            for number in range(0, len(dfAcademic)):

                c1 = ws.cell(row=var_est, column=1)
                c1.value = dfAcademic["Codigo"][number]
                c2 = ws.cell(row=var_est, column=2)
                c2.value = dfAcademic["Nombre"][number]
                c3 = ws.cell(row=var_est, column=3)
                c3.value = dfAcademic["Tipo"][number]
                c4 = ws.cell(row=var_est, column=4)
                c4.value = dfAcademic["Materia"][number]
                c5 = ws.cell(row=var_est, column=5)
                c5.value = dfAcademic["Promedio"][number]
                var_est += 1
            content = save_virtual_workbook(wb)
            response = HttpResponse(content)
            response['Content-Disposition'] = 'attachment; filename=informe_Academico.xlsx'
            response['Content-Type'] = 'application/x-xlsx'
            return response

        else:
            # informe financiero

            wb = Workbook()
            ws = wb.create_sheet(index=0, title="Financiero")

            headsList = list(dfFinance.columns.values)

            for number in range(0, len(headsList)):
                Heads = ws.cell(row=1, column=number + 1)
                Heads.value = headsList[number]

            var_est = 2
            for number in range(0, len(dfFinance)):

                c1 = ws.cell(row=var_est, column=1)
                c1.value = dfFinance["Codigo"][number]
                c2 = ws.cell(row=var_est, column=2)
                c2.value = dfFinance["Nombre"][number]
                c3 = ws.cell(row=var_est, column=3)
                c3.value = dfFinance["Tipo"][number]
                c4 = ws.cell(row=var_est, column=4)
                c4.value = dfFinance["Factura"][number]
                c5 = ws.cell(row=var_est, column=5)
                c5.value = dfFinance["Estado"][number]
                var_est += 1
            content = save_virtual_workbook(wb)
            response = HttpResponse(content)
            response['Content-Disposition'] = 'attachment; filename=informe_Financiero.xlsx'
            response['Content-Type'] = 'application/x-xlsx'
            return response
