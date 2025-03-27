from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from api_app.models.medico import Medico
from web_app.forms.medico import MedicoForm

class MedicoListView(ListView):
    model = Medico
    template_name = 'medico/listar.html'
    context_object_name = 'medicos'


class MedicoCreateView(CreateView):
    model = Medico
    form_class = MedicoForm
    template_name = 'medico/registrar.html'
    success_url = reverse_lazy('listar_medicos')


