from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
     path("resultados/", views.resultados, name="resultados"),
     path("errores/", views.errores, name="errores"),
]
