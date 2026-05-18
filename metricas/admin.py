from django.contrib import admin

from .models import metrica_errores, metrica_resultados, metrica_front

admin.site.register(metrica_errores)
admin.site.register(metrica_resultados)
admin.site.register(metrica_front)