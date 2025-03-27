from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from web_app.models.paciente import Paciente
from web_app.forms.paciente import PacienteForm

class PacienteListView(ListView):
    model = Paciente
    template_name = 'paciente/listar.html'
    context_object_name = 'pacientes'


class PacienteCreateView(CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'paciente/registrar.html'
    success_url = reverse_lazy('listar_pacientes')
