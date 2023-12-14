from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ImproperlyConfigured
from .models import *
from django.db.models import Q

import random
from datetime import datetime
import json



class ManagerUsers(BaseUserManager, models.Manager):

    #Manager para el modelo de usuarios se encuentra ok

    def create_user(self, codigo,tipe, username,nombres, apellidos, email, password, is_superuser, is_active, is_staff):

        usuario = self.model(
            codigo = codigo,
            username = username,
            nombres=nombres,
            apellidos=apellidos,
            email = email,
            is_superuser = is_superuser,
            is_active = is_active,
            is_staff = is_staff,
            tipe=tipe,

        )
        usuario.set_password(password)
        usuario.save(using = self.db)
        return usuario
    
    def create_superuser(self, username, email, password, tipe, nombres, apellidos):

        codigo =  self.model.objects.code_generator()

        usuario = self.model(
            codigo = codigo,
            username = username,
            nombres=nombres,
            apellidos=apellidos,
            email = email,
            tipe_id= int(tipe),
            is_superuser = True,
            is_active = True,
        )
        usuario.set_password(password)
        usuario.save(using = self.db)
        return usuario
    
    def code_generator(self):  
        try:
            filtro = self.latest('created_at').codigo
            cod_asign = int(filtro) + 1
            return str(cod_asign)
        except:
            cod_asign = 1000
            return str(cod_asign)
        
    def filtrar(self, order):

        if order == 'activos':
            consulta = self.filter(
                    is_active=True
            ).exclude(tipe_id__in=[4,5])
        elif order == 'inactivos':
            consulta = self.filter(
                    is_active = False
            ).exclude(tipe_id__in=[4,5])
        else:
            consulta = self.all().exclude(tipe_id__in=[4,5])
        
        return consulta.order_by('-codigo')

### Manager para los periodos, se encuentra ok
class periodoManager(models.Manager):

    def create_periodo(self, periodo):
        periodo= self.model(
            periodo = periodo,
        )
        periodo.save(using = self.db)
        return periodo
         


### Manager para los buscadores
class BuscadorManager(models.Manager):

    def create_periodo(self, periodo):
        periodo= self.model(
            periodo = periodo,
        )
        periodo.save(using = self.db)
        return periodo

    def code_invoice(self):
        try:
            filtro = self.latest('id').codigo
            cod_asign = int(filtro) + 1
        except:
            cod_asign = 100000

        return str(cod_asign)


    def code_generatorr(self):  
        try:
            filtro = self.latest('id').codigo
            cod_asign = int(filtro) + 1
        except:
            cod_asign = 1000

        return str(cod_asign)  
    

    # se encuentra ok, genera codigos de programas
    def code_programas(self):

        try:
            filtro = self.latest('id').cod_prog
            cod_asign = int(filtro) + 1
        except:
            año = datetime.now()
            cod_asign = str(año.year) + str(1000)

        return str(cod_asign)


    def filtrar_buscador(self, kword):

        consulta = self.filter(

            Q(cod_prog__icontains=kword) |
            Q(programa_name__icontains=kword)

        ).distinct()

        return consulta.order_by('-cod_prog')

    def filtrar_buscador_materias(self, kword):

        
        consulta = self.filter(

            Q(codigo__icontains=kword) |
            Q(materia__nombre_materia__icontains=kword) |
            Q(programa__programa_name__icontains=kword)
        ).distinct()

        return consulta.order_by('-codigo')
    
    def filtrar_student(self, kword, order):

        if order:
            if order == 'activos':
                consulta = self.filter(
                    is_active=True
                )
            elif order == 'inactivos':
                consulta = self.filter(
                    is_active = False
                )
            else:
                consulta = self.all()
        
        else:
            consulta = self.filter(
                Q(codigo__icontains=kword) |
                Q(apellidos__icontains=kword) |
                Q(nombre__icontains=kword) |
                Q(carrera__programa_name__icontains=kword)
            ).distinct()
        return consulta.order_by('-codigo')
    
    def filtrar_teacher(self, kword, order):

        if order:
            if order == 'activos':
                consulta = self.filter(
                    is_active=True
                )
            elif order == 'inactivos':
                consulta = self.filter(
                    is_active = False
                )
            else:
                consulta = self.all()
        
        else:
            consulta = self.filter(
                Q(codigo__icontains=kword) |
                Q(apellidos__icontains=kword) |
                Q(nombres__icontains=kword)
            ).distinct()

        return consulta.order_by('-codigo')

    def filtrar_buscador_Teacher_topic(self, kword, cod):
        consulta = self.filter(docente=cod).filter(
                Q(codigo__icontains=kword) |
                Q(materia__nombre_materia__icontains=kword) |
                Q(programa__programa_name__icontains=kword) |
                Q(periodo__periodo__icontains=kword)

            ).distinct()
        return consulta.order_by('periodo')
    
    def filtrar_buscador_Teacher_notes(self, kword, cod):
        consulta = self.filter(materia=cod).filter(
                Q(cod_student__codigo__icontains=kword) |
                Q(cod_student__nombre__icontains=kword) |
                Q(cod_student__apellidos__icontains=kword)

            ).distinct()
        return consulta.order_by('cod_student')
    

    ########
    def crear(self, tipe, cod_prog, programa_name, aceptado, matricula, cuota_valor, cuotas, costo):

        programa = self.model(
            cod_prog= cod_prog,
            programa_name= programa_name,
            aceptado= aceptado,
            matricula=matricula,
            cuota_valor=cuota_valor,
            cuotas=cuotas,
            costo=costo,
            is_active = True,
            tipe = tipe,
            
        )
        programa.save(using = self.db)
        return programa
    
    def manejo(self, valor1, valor2):
        try:

            valor = float(valor1.monto)-float(valor2)
        except:
            valor= int(valor1.monto)
        return valor

    def manejo2(self,valor2):
        if valor2 is not None:
            return valor2
        else:
            return 0.0
        
        
    def get_secret(self, secret_name):
        with open('secret.json') as f:
           secrets= json.loads(f.read())
        try:
            return secrets[secret_name]
        except:
            mgs= 'la variable %s no existe' % secret_name
            raise ImproperlyConfigured(mgs)
        
    def mes(self, var):
        if var.month <=7:
            return "1"
        else:
            return "2"
        
    



