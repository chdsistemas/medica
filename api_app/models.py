from django.db import models
from django.contrib.auth.models import AbstractUser

class Persona(AbstractUser):
    documento = models.CharField(max_length=100, unique=True, verbose_name='Número de documento personal')
    ciudad_residencia = models.CharField(max_length=100, verbose_name='Ciudad de residencia')
    telefono = models.CharField(max_length=100, verbose_name='telefono')

    def __str__(self):
        return (f'{self.first_name} -{self.last_name}')
    
    
    


