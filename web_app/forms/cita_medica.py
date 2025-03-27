from django import forms
from api_app.models.cita_medica import CitaMedica

class CitaMedicaForm(forms.ModelForm):
    class Meta:
        model = CitaMedica
        fields = '__all__'

