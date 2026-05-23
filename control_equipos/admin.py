from django.contrib import admin
from .models import Equipo


@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):

    list_display = (
        'tipo',
        'marca',
        'serial',
        'estado',
        'nombre_estudiante',
        'numero_estudiante',
        'fecha_solicitud',
    )

    list_filter = (
        'tipo',
        'estado',
    )

    search_fields = (
        'serial',
        'marca',
        'nombre_estudiante',
        'numero_estudiante',
    )

    ordering = (
        'tipo',
    )