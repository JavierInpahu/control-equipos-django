from django.db import models


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

    def __str__(self):
        return f"{self.marca} - {self.serial}"