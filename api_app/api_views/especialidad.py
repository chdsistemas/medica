from rest_framework import viewsets
from api_app.models.especialidad import Especialidad
from api_app.serializers.especialidad import EspecialidadSerializer

class EspecialidadViewSet(viewsets.ModelViewSet):
    
    # API para gestionar especialidades médicas.
    # CRUD completo del modelo
    
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer
    