from django.db import models
from api_app.models.persona import Persona
from api_app.models.especialidad import Especialidad

class Medico(Persona):
    carnet = models.CharField(max_length=50, verbose_name='Número de carnet médico')
    especialidad = models.ForeignKey(Especialidad, on_delete=models.PROTECT)

    class Meta:
        db_table = 'medicos'

    def __str__(self):
        return (f'{self.first_name}-{self.last_name}')