from django import forms
from web_app.models.medico import Medico

class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ['documento', 'username', 'first_name', 'last_name', 'ciudad_residencia', 'telefono', 'email', 'especialidad']


