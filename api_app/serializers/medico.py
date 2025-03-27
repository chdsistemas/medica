from rest_framework import serializers
from web_app.models.medico import Medico

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = ['documento', 'username', 'first_name', 'last_name', 'ciudad_residencia', 'telefono', 'email', 'especialidad']
        #fields = '__all__'


