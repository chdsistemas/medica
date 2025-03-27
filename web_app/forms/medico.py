from django import forms
from api_app.models.medico import Medico

class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = '__all__'


