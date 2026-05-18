from django.contrib import admin
from .models import Equipo


@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):

    list_display = (
        'tipo',
        'marca',
        'serial',
        'estado',
        'fecha_compra',
    )

    list_filter = (
        'tipo',
        'estado',
    )

    search_fields = (
        'serial',
        'marca',
    )

    ordering = (
        'tipo',
    )