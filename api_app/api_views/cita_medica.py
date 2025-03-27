from rest_framework import viewsets
from api_app.models.cita_medica import CitaMedica
from api_app.serializers.cita_medica import CitaMedicaSerializer

class CitaMedicaViewSet(viewsets.ModelViewSet):
    
    # API para gestionar citas médicas.
    # CRUD completo del modelo
    
    queryset = CitaMedica.objects.all()
    serializer_class = CitaMedicaSerializer

    