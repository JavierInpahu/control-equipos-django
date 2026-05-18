from django.urls import path
from . import views
from . import views_tests

urlpatterns = [
    path("equipos/", views.EquipoListView.as_view(), name="equipo_list"),
    path("equipo/nuevo/", views.EquipoCreateView.as_view(), name="equipo_create"),
    path("equipo/<int:pk>/", views.EquipoDetailView.as_view(), name="equipo_detail"),
    path("equipo/<int:pk>/editar/", views.EquipoUpdateView.as_view(), name="equipo_update"),
    path("equipo/<int:pk>/eliminar/", views.EquipoDeleteView.as_view(), name="equipo_delete"),

    path("tests/", views_tests.crud_test_dashboard, name="crud_test_dashboard"),
]