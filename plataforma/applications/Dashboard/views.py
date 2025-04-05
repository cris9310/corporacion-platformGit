from django.shortcuts import HttpResponseRedirect
from django.views.generic import (TemplateView,ListView, View)
from django.db.models import Sum, F
from django.utils import timezone
from django.db.models.functions import TruncMonth
from django.urls import reverse_lazy
from django.utils.timezone import now
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_control

import pandas as pd
from dateutil.relativedelta import relativedelta

from applications.User.mixins import *
from applications.Student.models import *
from applications.Finance.models import *
from applications.Programs.models import *



def RedirectUserView(request):

    if request.user.is_authenticated and request.user.tipe.rol == 'Administrador' or request.user.tipe.rol == 'Gestor':
        return HttpResponseRedirect(
            reverse_lazy('dashboard_app:dashboard-admin')
            )
    elif request.user.is_authenticated and request.user.tipe.rol == 'Estudiante':
        return HttpResponseRedirect(
            reverse_lazy('student_app:student-my-notes')
            )
    
    elif request.user.is_authenticated and request.user.tipe.rol == 'Docente':
        return HttpResponseRedirect(
            reverse_lazy('teacher_app:teacher-my-own-topic-list')
            )
    
    else:
        return HttpResponseRedirect(
            reverse_lazy('teacher_app:teacher-list-Coordinator')
        )
    

@method_decorator(cache_control(no_cache=True, must_revalidate=True, no_store=True), name='dispatch')
class DashboardAdminView(AdminRequiredMixin, TemplateView):
    template_name = "dashboard/dashboard_admin.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        activos = Estudiante.objects.filter(is_active=True).count()
        
        #------------------------- ingresos y gastos del mes -------------------------------------
        nowA = timezone.now()
        mes = nowA.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        ingresosMensualidades = FacturasSub.objects.filter(created_at__gte=mes).aggregate(total_ingresos=Sum('pagado'))['total_ingresos'] or 0
        otrosIngresos = OtroIngreso.objects.filter(fecha__gte=mes).aggregate(total_ingresos=Sum('monto'))['total_ingresos'] or 0
        gastos = Gastos.objects.filter(fecha__gte=mes).aggregate(total_gastos=Sum('monto'))['total_gastos'] or 0
        nomina = Nominas.objects.filter(fecha__gte=mes).aggregate(total_nomina=Sum('monto'))['total_nomina'] or 0
        gastos = float(gastos) + float (nomina)
        totalIngresoMes = float(ingresosMensualidades) + float(otrosIngresos)

        inicioAnio = nowA.replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
        ingresosAnualesMensualidades = FacturasSub.objects.filter(created_at__gte=inicioAnio).aggregate(total_ingresos=Sum('pagado'))['total_ingresos'] or 0
        otrosIngresosAnuales = OtroIngreso.objects.filter(fecha__gte=inicioAnio).aggregate(total_ingresos=Sum('monto'))['total_ingresos'] or 0
        gastosAnio = Gastos.objects.filter(fecha__gte=inicioAnio).aggregate(total_gastos=Sum('monto'))['total_gastos'] or 0
        nominaAnio = Nominas.objects.filter(fecha__gte=inicioAnio).aggregate(total_nominas=Sum('monto'))['total_nominas'] or 0
        gastosAnio = float(gastosAnio) + float(nominaAnio)
        totalIngresosAnio= ingresosAnualesMensualidades + otrosIngresosAnuales

        #------------------------indicador de cartera-----------------------------------------
        facturas_vencidas = Facturas.objects.filter(estado_id=4)
        monto_vencido = facturas_vencidas.annotate(
            saldo_pendiente=F('monto') - (
                FacturasSub.objects.filter(facturas=F('id')).aggregate(pagado_total=Sum('pagado'))['pagado_total'] or 0
            )
        ).aggregate(total_vencido=Sum('saldo_pendiente'))['total_vencido'] or 0
        monto_total = Facturas.objects.filter(due_at__lt=nowA).aggregate(total_facturado=Sum('monto'))['total_facturado'] or 0
        indicador_cartera_vencida = (
            f"{round((monto_vencido / monto_total) * 100, 2)} %" if monto_total > 0 else "0 %"
        )
        #--------------------------------Gráficas de los ingresos y gastos-------------------------------------------------------
        current_time = now()
        inicio_rango = current_time.replace(year=current_time.year - 1, day=1, month=1)

        # Generar todos los meses dentro del rango
        meses = [(inicio_rango + relativedelta(months=i)).strftime('%y/%m') for i in range(12)]

        # Base inicial para ingresos y gastos
        lista_base = [{'mes': mes, 'valor': 0, 'concepto': 'ingresos'} for mes in meses]
        lista_base += [{'mes': mes, 'valor': 0, 'concepto': 'gastos'} for mes in meses]

        # Consultas para ingresos y gastos
        ingresos = (
            FacturasSub.objects.filter(created_at__range=(inicio_rango, current_time))
            .annotate(mes=TruncMonth('created_at'))
            .values('mes')
            .annotate(total=Sum('pagado'))
            .order_by('mes')
        )

        otros_ingresos = (
            OtroIngreso.objects.filter(fecha__range=(inicio_rango, current_time))
            .annotate(mes=TruncMonth('fecha'))
            .values('mes')
            .annotate(total=Sum('monto'))
            .order_by('mes')
        )

        gastos_grafico = (
            Gastos.objects.filter(fecha__range=(inicio_rango, current_time))
            .annotate(mes=TruncMonth('fecha'))
            .values('mes')
            .annotate(total=Sum('monto'))
            .order_by('mes')
        )

        nominas_grafico = (
            Nominas.objects.filter(fecha__range=(inicio_rango, current_time))
            .annotate(mes=TruncMonth('fecha'))
            .values('mes')
            .annotate(total=Sum('monto'))
            .order_by('mes')
        )

        # Convertir resultados de consultas a lista
        lista = []

        for ingreso in ingresos:
            lista.append({'mes': ingreso['mes'].strftime('%y/%m'), 'valor': ingreso['total'], 'concepto': 'ingresos'})

        for otro_ingreso in otros_ingresos:
            lista.append({'mes': otro_ingreso['mes'].strftime('%y/%m'), 'valor': otro_ingreso['total'], 'concepto': 'ingresos'})

        for gasto in gastos_grafico:
            lista.append({'mes': gasto['mes'].strftime('%y/%m'), 'valor': gasto['total'], 'concepto': 'gastos'})

        for nomina in nominas_grafico:
            lista.append({'mes': nomina['mes'].strftime('%y/%m'), 'valor': nomina['total'], 'concepto': 'gastos'})

        # Crear DataFrame base
        df_base = pd.DataFrame(lista_base)

        # Validar si hay datos; si no, se agrega un registro base
        if not lista:
            lista.append({'mes': current_time.strftime('%y/%m'), 'valor': 0, 'concepto': 'gastos'})

        df_datos = pd.DataFrame(lista)
        df_datos['valor'] = df_datos['valor'].astype(int)

        # Combinar DataFrame base y datos calculados
        df_completo = pd.concat([df_base, df_datos]).groupby(['mes', 'concepto'])['valor'].sum().reset_index()

        # Convertir a JSON
        ingresosGastosGrafica = df_completo.to_json(orient="records")

        #---------------------------franja de indicadores de programas------------

        programas =  Programas.objects.all()
        listaprogramas=[]

        for i in programas:
            totalMatriculados=Estudiante.objects.filter(carrera_id=i.pk).count()
            totalGraduados=Graduated.objects.filter(student__carrera_id=i.pk).count()
            datosProgramas={'programa':i.programa_name, 'totalMatriculados':totalMatriculados, 
                            'totalGraduados':totalGraduados, 'variacion':(totalGraduados / totalMatriculados) * 100 
                            if totalMatriculados > 0 else 0}
            listaprogramas.append(datosProgramas)
        dfprogramas= pd.DataFrame(listaprogramas)
        dfprogramas=dfprogramas.to_json(orient="records")


        #----------------------Docentes------------------------

        docentes = Docente.objects.all()
        listaDocentes=[]
        for i in docentes:
            totalAsignaturas = Materias.objects.filter(docente_id=i.pk).count()
            datosDocentes={"docente":i.nombres + " " + i.apellidos, 'total': totalAsignaturas}
            listaDocentes.append(datosDocentes)
        listaDocentesOrganizada = sorted(listaDocentes, key=lambda x: x["total"], reverse=False)
        dfdocentes = listaDocentesOrganizada[:10]
        

        #------------------------Contextos-----------------------------------------------------------

        context['IndIniciales'] ={'icvdinero': f'$ {monto_vencido:,.0f}', 'icv': indicador_cartera_vencida,
                                  'totalIngresoMes': f'$ {totalIngresoMes:,.0f}', 'totalGastos': f'$ {gastos:,.0f}',
                                  "activos": activos, 'totalIngresosAnio':f'$ {totalIngresosAnio:,.0f}',
                                  'gastosAnio':f'$ {gastosAnio:,.0f}'}
        
        context['ingresosGastosGrafica'] = ingresosGastosGrafica
        context['dfprogramas'] = dfprogramas
        context['dfdocentes'] = dfdocentes
        
        return context
    

