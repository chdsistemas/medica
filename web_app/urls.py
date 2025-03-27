from django.urls import path
from web_app.views.medico import MedicoListView, MedicoCreateView
from web_app.views.paciente import PacienteListView, PacienteCreateView

urlpatterns = [
    path('medico/listar/', MedicoListView.as_view(), name='listar_medicos'),
    path('medico/registrar/', MedicoCreateView.as_view(), name='registrar_medico'),
    path('paciente/listar/', PacienteListView.as_view(), name='listar_pacientes'),
    path('paciente/registrar/', PacienteCreateView.as_view(), name='registrar_paciente'),
]




