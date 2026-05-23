from django.db import models
from django.core.validators import RegexValidator


class Equipo(models.Model):

    class Tipo(models.TextChoices):
        COMPUTADOR = "COMPUTADOR", "Computador"
        HDMI = "HDMI", "HDMI"
        CONTROL = "CONTROL", "Control"
        TECLADO = "TECLADO", "Teclado"
        MOUSE = "MOUSE", "Mouse"
        PROYECTOR = "PROYECTOR", "Proyector"

    class Estado(models.TextChoices):
        DISPONIBLE = "DISPONIBLE", "Disponible"
        EN_USO = "EN_USO", "En uso"
        DAÑADO = "DAÑADO", "Dañado"
        MANTENIMIENTO = "MANTENIMIENTO", "Mantenimiento"

    marca = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=Tipo.choices)
    serial = models.CharField(max_length=100)
    estado = models.CharField(max_length=20, choices=Estado.choices)
    fecha_compra = models.DateField()

    nombre_estudiante = models.CharField(
        max_length=200,
        blank=True,
        default=""
    )

    numero_estudiante = models.CharField(
        max_length=15,
        blank=True,
        default="",
        validators=[
            RegexValidator(
                regex=r'^\d{15}$',
                message='El número de estudiante debe contener exactamente 15 dígitos.'
            )
        ]
    )

    def __str__(self):
        return f"{self.marca} - {self.serial}"