
import os
import sys
import django

# Agregar el directorio raíz del proyecto al PYTHONPATH
sys.path.append("C:/Users/crist/OneDrive/Escritorio/corporacion-platformGit/corporacion-platformGit/plataforma")

# Configurar el entorno de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "plataforma.settings")
django.setup()

from applications.Finance.models import *

def actualizar_estados_facturas():
        # Obtén la fecha actual
        hoy = timezone.now()

        
        facturas_pendientes = Facturas.objects.filter(
            estado__in=[1, 2],  
            due_at__lt=hoy  
        )

        facturas_pendientes.update(estado_id=4)

actualizar_estados_facturas()