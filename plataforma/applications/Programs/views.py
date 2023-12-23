from typing import Any, Dict
from django.shortcuts import render
import datetime
from openpyxl import Workbook
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.writer.excel import save_virtual_workbook
from decimal import *
import warnings


from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.db.models.functions import Coalesce
from django.db.models import F, Sum, Avg, Count

# Create your views here.

from .models import *
from django.views.generic import (TemplateView,
                                  FormView, CreateView, DeleteView, UpdateView,
                                  DetailView, ListView, View)


from .forms import *
from django.urls import reverse_lazy, reverse
import pandas as pd
import re


# Vista ok
class ConfigTemplateView(TemplateView):
    template_name = "configuraciones/setings.html"


#------- periodos ---------
class PeriodoCreateView(CreateView):
    model = Periodos
    form_class = PeriodoForm
    template_name = 'periodos/register_periodo.html'
    success_url = reverse_lazy('settings_app:list-periodo')

    def post(self, request, *args, **kwargs):
        form = PeriodoForm(self.request.POST)
        
        if form.is_valid():
            periodo = str(form.cleaned_data.get('periodo')),
            create_peri = Periodos.objects.create_periodo(
            periodo[0],
            )
            mensaje = f'{self.model.__name__} creado correctamente'
            error = "No hay error!"
            response = JsonResponse({"mensaje": mensaje, "error": error})
            response.status_code = 201
            return response
        else:
            mensaje1 =[]
            mensaje1.append(
                {"error": form.errors}
            )
            response = JsonResponse(mensaje1, safe=False)
            response.status_code = 400
            return response

class PeriodoListView(ListView):
    model = Periodos
    template_name = 'periodos/list_periodos.html'
    context_object_name = 'periodos'

    def get_queryset(self):

        data_periodos = Periodos.objects.all()
        data = []
        for i in data_periodos:
            if Materias.objects.filter(periodo_id=i.id):
                data_json = {"id": i.id, "periodo": i.periodo, "estado": True}
                data.append(data_json)
            else:
                data_json = {"id": i.id, "periodo": i.periodo, "estado": False}
                data.append(data_json)

        return data


class PeriodoDeleteView(DeleteView):
    template_name = 'periodos/detele_periodo.html'
    model = Periodos
    success_url = reverse_lazy('settings_app:list-periodo')




#------- programas ---------


#Vista de creacion de programas ok
class ProgramaCreateView(CreateView):
    model = Programas
    form_class = ProgramaForm
    template_name = 'programas/register_program.html'
    success_url = reverse_lazy('settings_app:list-program')

    def post(self, request, *args, **kwargs):

        form = ProgramaForm(self.request.POST)
        
        if form.is_valid():

            crear_programa = Programas.objects.crear(
                tipe=form.cleaned_data['tipe'],
                cod_prog=Programas.objects.code_programas(),
                matricula=form.cleaned_data['matricula'],
                cuota_valor=form.cleaned_data['cuota_valor'],
                cuotas=form.cleaned_data['cuotas'],
                costo=form.cleaned_data['costo'],
                programa_name=form.cleaned_data['programa_name'],
                aceptado=form.cleaned_data['aceptado']

            )
            mensaje = f'{self.model.__name__} creado correctamente'
            error = "No hay error!"
            response = JsonResponse({"mensaje": mensaje, "error": error})
            response.status_code = 201
            return response
        else:
            mensaje1 =[]
            mensaje1.append(
                {"error": form.errors}
            )
            response = JsonResponse(mensaje1, safe=False)
            response.status_code = 400
            return response


#Vista de detalle de programas ok
class ProgramaDetailView(DetailView):
    template_name = 'programas/detail_program.html'
    model = Programas


    def get_context_data(self, **kwargs):
        context = super( ProgramaDetailView, self).get_context_data(**kwargs)
        datos = Programas.objects.get(
            pk=self.kwargs['pk'])
        datos_final = {"cod_prog": datos.cod_prog, 'programa_name': datos.programa_name,
                'matricula': f'$ {datos.matricula:,.2f}', 'costo': f'$ {datos.costo:,.2f}', 'cuota_valor': datos.cuota_valor,
                "cuotas": f'$ {datos.cuotas:,.2f}'
            }

        context['datos'] = datos_final
        return context



#Vista de eliminacion de programas ok
class ProgramaDeleteView(DeleteView):
    template_name = 'programas/delete_program.html'
    model = Programas
    success_url = reverse_lazy('settings_app:list-program')

#Vista de actualizacion de programas ok
class ProgramaUpdateView(UpdateView):
    template_name = 'programas/update_program.html'
    model = Programas
    form_class = ProgramaForm
    success_url = reverse_lazy('settings_app:list-program')

#Vista de listado de programas ok
class Programalistview(ListView):
    model = Programas
    template_name = 'programas/list_programas.html'
    context_object_name = 'programas'

    def get_queryset(self):
        kword = self.request.GET.get('kword', '')
        data_program = []
        if kword:
            data_prin = Programas.objects.filtrar_buscador(kword)
            for i in data_prin:
                if Materias.objects.filter(programa_id=i.id).exists():
                    data_json = {"pk": i.id, "codigo": i.cod_prog,
                                 "programa": i.programa_name, "estado": True, "is_active": i.is_active}
                    data_program.append(data_json)
                else:
                    data_json = {"pk": i.id, "codigo": i.cod_prog,
                                 "programa": i.programa_name, "estado": False, "is_active": i.is_active}
                    data_program.append(data_json)
            queryset = data_program

        else:

            data_prin = Programas.objects.all()
            for i in data_prin:
                if Materias.objects.filter(programa_id=i.id).exists():
                    data_json = {"pk": i.id, "codigo": i.cod_prog,
                                 "programa": i.programa_name, "estado": True, "is_active": i.is_active}
                    data_program.append(data_json)
                else:
                    data_json = {"pk": i.id, "codigo": i.cod_prog,
                                 "programa": i.programa_name, "estado": False, "is_active": i.is_active}
                    data_program.append(data_json)
            queryset = data_program

        return queryset
