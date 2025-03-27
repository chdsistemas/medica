from rest_framework import viewsets
from web_app.models.paciente import Paciente
from api_app.serializers.paciente import PacienteSerializer

class PacienteViewSet(viewsets.ModelViewSet):
    
    # API para gestionar pacientes.
        
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

    