from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Equipo
from .forms import EquipoForm


class EquipoListView(ListView):
    model = Equipo
    template_name = "control_equipos/equipo_list.html"
    context_object_name = "equipos"


class EquipoDetailView(DetailView):
    model = Equipo
    template_name = "control_equipos/equipo_detail.html"


class EquipoCreateView(CreateView):
    model = Equipo
    form_class = EquipoForm
    template_name = "control_equipos/equipo_form.html"
    success_url = reverse_lazy("equipo_list")


class EquipoUpdateView(UpdateView):
    model = Equipo
    form_class = EquipoForm
    template_name = "control_equipos/equipo_form.html"
    success_url = reverse_lazy("equipo_list")


class EquipoDeleteView(DeleteView):
    model = Equipo
    template_name = "control_equipos/equipo_confirm_delete.html"
    success_url = reverse_lazy("equipo_list")