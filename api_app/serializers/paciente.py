from rest_framework import serializers
from web_app.models.paciente import Paciente

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ['documento', 'username', 'first_name', 'last_name', 'ciudad_residencia', 'telefono', 'email', 'tipo']

