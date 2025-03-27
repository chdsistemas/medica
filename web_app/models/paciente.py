from django.db import models
from web_app.models.persona import Persona

class Paciente(Persona):
    TIPO = [
        ('PREMIUM', 'Paciente Premium'),
        ('GENERAL', 'Paciente General')
    ]
    tipo = models.CharField(max_length=20, choices=TIPO, default='GENERAL')


    class Meta:
        db_table = 'pacientes'


    def __str__(self):
        return (f'{self.first_name}-{self.last_name}')
    
