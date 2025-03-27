from django import forms
from web_app.models.paciente import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['documento', 'username', 'first_name', 'last_name', 'ciudad_residencia', 'telefono', 'email', 'tipo']

        