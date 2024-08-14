from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(CatalogsTypesActivities)
admin.site.register(CatalogsSede)
admin.site.register(CatalogsJornada)
admin.site.register(CatalogsTypesDocuement)
admin.site.register(CatalogsTypesProg)
admin.site.register(CatalogsTypesRol)