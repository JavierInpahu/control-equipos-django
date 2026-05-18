from django import forms
from .models import Equipo
from datetime import date


TIPOS_EQUIPO = [
    ('COMPUTADOR', 'Computador'),
    ('HDMI', 'HDMI'),
    ('CONTROL', 'Control'),
    ('TECLADO', 'Teclado'),
    ('MOUSE', 'Mouse'),
    ('PROYECTOR', 'Proyector'),
]

ESTADOS_EQUIPO = [
    ('DISPONIBLE', 'Disponible'),
    ('EN_USO', 'En uso'),
    ('DAÑADO', 'Dañado'),
    ('MANTENIMIENTO', 'Mantenimiento'),
]


class EquipoForm(forms.ModelForm):

    tipo = forms.ChoiceField(choices=TIPOS_EQUIPO)
    estado = forms.ChoiceField(choices=ESTADOS_EQUIPO)

    class Meta:
        model = Equipo
        fields = ['marca', 'tipo', 'serial', 'estado', 'fecha_compra']
        widgets = {
            'fecha_compra': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_fecha_compra(self):
        fecha = self.cleaned_data.get("fecha_compra")

        if fecha and fecha > date.today():
            raise forms.ValidationError("La fecha de compra no puede ser mayor a hoy")

        return fecha