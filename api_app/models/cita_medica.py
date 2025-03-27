from django.db import models
from api_app.models.paciente import Paciente
from api_app.models.medico import Medico

class CitaMedica(models.Model):
    codigo = models.CharField(max_length=50, verbose_name='Código de la cita médica')
    ciudad = models.CharField(max_length=50, verbose_name='Ciudad de atención')
    direccion = models.CharField(max_length=50, verbose_name='Dirección postal del lugar de atención')
    fecha = models.DateField(verbose_name='Hora en formato yyyy-mm-dd')
    hora = models.TimeField(verbose_name='Hora de la cita formato 24H 00:00:00')
    medico = models.ForeignKey(Medico, on_delete=models.PROTECT)
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT)

    class Meta:
        db_table = 'citas_medicas'

    