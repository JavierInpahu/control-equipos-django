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
        fields = [
            'marca',
            'tipo',
            'serial',
            'estado',
            'fecha_compra',
            'nombre_estudiante',
            'numero_estudiante',
        ]

        widgets = {
            'fecha_compra': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_fecha_compra(self):
        fecha = self.cleaned_data.get("fecha_compra")

        if fecha and fecha > date.today():
            raise forms.ValidationError(
                "La fecha de compra no puede ser mayor a hoy"
            )

        return fecha

    def clean_numero_estudiante(self):
        numero = self.cleaned_data.get("numero_estudiante")

        if numero:

            if not numero.isdigit():
                raise forms.ValidationError(
                    "El número de estudiante solo puede contener números."
                )

            if len(numero) != 15:
                raise forms.ValidationError(
                    "El número de estudiante debe contener exactamente 15 dígitos."
                )

        return numero