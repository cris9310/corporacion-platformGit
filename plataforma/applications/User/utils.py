
import os


import django
from django.core.management import call_command

from .manager import actualizar_estados_facturas

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mi_proyecto.settings")
django.setup()

actualizar_estados_facturas()