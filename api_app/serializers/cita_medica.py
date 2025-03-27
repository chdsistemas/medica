from rest_framework import serializers
from api_app.models.cita_medica import CitaMedica

class CitaMedicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CitaMedica
        fields = '__all__'

        