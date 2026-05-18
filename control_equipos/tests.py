from django.test import TestCase
from django.urls import reverse
from .models import Equipo


class EquipoModelTest(TestCase):

    def setUp(self):
        self.equipo = Equipo.objects.create(
            marca="HP",
            tipo="COMPUTADOR",
            serial="HP123",
            estado="DISPONIBLE",
            fecha_compra="2026-05-17"
        )

    def test_creacion_equipo(self):
        self.assertEqual(self.equipo.marca, "HP")
        self.assertEqual(self.equipo.serial, "HP123")


class EquipoViewsTest(TestCase):

    def setUp(self):
        self.equipo = Equipo.objects.create(
            marca="DELL",
            tipo="COMPUTADOR",
            serial="DL001",
            estado="DISPONIBLE",
            fecha_compra="2026-05-17"
        )

    def test_lista_equipos(self):
        response = self.client.get(reverse("equipo_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "DELL")

    def test_detalle_equipo(self):
        response = self.client.get(reverse("equipo_detail", args=[self.equipo.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "DL001")

    def test_crear_equipo_get(self):
        response = self.client.get(reverse("equipo_create"))
        self.assertEqual(response.status_code, 200)