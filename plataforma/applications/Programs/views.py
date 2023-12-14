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

from .funciones import generador
# Create your views here.

from .models import *
from Applications.agenda.models import *
from Applications.financiero.models import *
from django.views.generic import (TemplateView,
                                  FormView, CreateView, DeleteView, UpdateView,
                                  DetailView, ListView, View)


from .forms import *
from django.urls import reverse_lazy, reverse
from .choices import EST_STUDENT
import pandas as pd
import re


# Vista ok
class ConfigTemplateView(TemplateView):
    template_name = "configuraciones/setings.html"


#------- periodos ---------
class PeriodoCreateView(FormView):
    form_class = PeriodoForm
    template_name = 'periodos/register_periodo.html'
    success_url = reverse_lazy('settings_app:config')

    def form_valid(self, form):
        periodo = str(form.cleaned_data['periodo']),
        create_peri = Periodos.objects.create_periodo(
            periodo[0],

        )
        return HttpResponseRedirect(self.success_url)


class PeriodoListView(ListView):
    model = Periodos
    template_name = 'periodos/list_periodos.html'
    context_object_name = 'periodos'
    paginate_by = 5

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