from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ImproperlyConfigured
from django.utils.text import slugify

from datetime import datetime
import json
import uuid

from .models import *



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


    def code_invoice(self):
        try:
            filtro = self.latest('id').codigo
            cod_asign = int(filtro) + 1
        except:
            cod_asign = 100000

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
    
    def code_task(self):

        try:
            filtro = self.latest('id').cod_tarea
            cod_asign = int(filtro) + 1
        except:
            cod_asign = str(1000)

        return str(cod_asign)
    
    def code_asignaturas(self):

        try:
            filtro = self.latest('id').codigo
            cod_asign = int(filtro) + 1
        except:
            año = datetime.now()
            cod_asign = str(año.year) + str(2000)

        return str(cod_asign)

    

    
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
        
    def generate_unique_slug(self,base_value, existing_slugs):
        slug = f"{slugify(base_value)}-{uuid.uuid4().hex[:8]}"
        while slug in existing_slugs:
            slug = f"{slugify(base_value)}-{uuid.uuid4().hex[:8]}"
        existing_slugs.add(slug)
        return slug
    



        
    

    
