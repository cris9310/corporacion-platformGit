from django.shortcuts import render
from django.views.generic import (TemplateView,ListView, View)
from django.db.models import Sum, F
from django.utils import timezone
from django.db.models.functions import TruncMonth


import pandas as pd
from dateutil.relativedelta import relativedelta

from applications.User.mixins import *
from applications.Student.models import *
from applications.Finance.models import *
from applications.Programs.models import *

class DashboardAdminView(AdminRequiredMixin, TemplateView):
    template_name = "dashboard/dashboard_admin.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        activos = Estudiante.objects.filter(is_active=True).count()
        
        #------------------------- ingresos y gastos del mes -------------------------------------
        now = timezone.now()
        mes = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        ingresosMensualidades = FacturasSub.objects.filter(created_at__gte=mes).aggregate(total_ingresos=Sum('pagado'))['total_ingresos'] or 0
        otrosIngresos = OtroIngreso.objects.filter(fecha__gte=mes).aggregate(total_ingresos=Sum('monto'))['total_ingresos'] or 0
        gastos = Gastos.objects.filter(fecha__gte=mes).aggregate(total_gastos=Sum('monto'))['total_gastos'] or 0
        totalIngresoMes = float(ingresosMensualidades) + float(otrosIngresos)

        inicioAnio = now.replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
        ingresosAnualesMensualidades = FacturasSub.objects.filter(created_at__gte=inicioAnio).aggregate(total_ingresos=Sum('pagado'))['total_ingresos'] or 0
        otrosIngresosAnuales = OtroIngreso.objects.filter(fecha__gte=inicioAnio).aggregate(total_ingresos=Sum('monto'))['total_ingresos'] or 0
        gastosAnio = Gastos.objects.filter(fecha__gte=inicioAnio).aggregate(total_gastos=Sum('monto'))['total_gastos'] or 0
        totalIngresosAnio= ingresosAnualesMensualidades + otrosIngresosAnuales

        #------------------------indicador de cartera-----------------------------------------
        facturas_vencidas = Facturas.objects.filter(estado_id=4)
        monto_vencido = facturas_vencidas.annotate(
            saldo_pendiente=F('monto') - (
                FacturasSub.objects.filter(facturas=F('id')).aggregate(pagado_total=Sum('pagado'))['pagado_total'] or 0
            )
        ).aggregate(total_vencido=Sum('saldo_pendiente'))['total_vencido'] or 0
        monto_total = Facturas.objects.filter(due_at__lt=now).aggregate(total_facturado=Sum('monto'))['total_facturado'] or 0
        indicador_cartera_vencida = str(round(((monto_vencido / monto_total)) * 100,2))+ " %"
        #--------------------------------Gráficas de los ingresos y gastos-------------------------------------------------------
       # Fecha de inicio del rango (mismo mes del año anterior)
        inicio_rango = now.replace(year=now.year - 1, day=1, month=now.month)

        # Generar todos los meses dentro del rango
        meses = [(inicio_rango + relativedelta(months=i)).strftime('%y/%m') for i in range(12)]

        # Base inicial para ingresos y gastos
        lista_base = [{'mes': mes, 'valor': 0, 'concepto': 'ingresos'} for mes in meses]
        lista_base += [{'mes': mes, 'valor': 0, 'concepto': 'gastos'} for mes in meses]

        # Consultas para ingresos y gastos
        ingresos = (
            FacturasSub.objects.filter(created_at__range=(inicio_rango, now))
            .annotate(mes=TruncMonth('created_at'))
            .values('mes')
            .annotate(total=Sum('pagado'))
            .order_by('mes')
        )

        otros_ingresos = (
            OtroIngreso.objects.filter(fecha__range=(inicio_rango, now))
            .annotate(mes=TruncMonth('fecha'))
            .values('mes')
            .annotate(total=Sum('monto'))
            .order_by('mes')
        )

        gastos_grafico = (
            Gastos.objects.filter(fecha__range=(inicio_rango, now))
            .annotate(mes=TruncMonth('fecha'))
            .values('mes')
            .annotate(total=Sum('monto'))
            .order_by('mes')
        )

        # Convertir resultados a una lista
        lista = []

        for i in ingresos:
            fecha = i['mes']
            valor = {'mes': fecha.strftime('%y/%m'), 'valor': i['total'], 'concepto': 'ingresos'}
            lista.append(valor)

        for i in otros_ingresos:
            fecha = i['mes']
            valor = {'mes': fecha.strftime('%y/%m'), 'valor': i['total'], 'concepto': 'ingresos'}
            lista.append(valor)

        for i in gastos_grafico:
            fecha = i['mes']
            valor = {'mes': fecha.strftime('%y/%m'), 'valor': i['total'], 'concepto': 'gastos'}
            lista.append(valor)

        df_base = pd.DataFrame(lista_base)

        df_datos = pd.DataFrame(lista)

        df_datos['valor'] = df_datos['valor'].astype(int)
        df_completo = pd.concat([df_base, df_datos]).groupby(['mes', 'concepto'])['valor'].sum().reset_index()
        ingresosGastosGrafica= df_completo.to_json(orient="records")

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
    

