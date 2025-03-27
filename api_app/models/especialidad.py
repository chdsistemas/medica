from django.db import models

class Especialidad(models.Model):
    codigo = models.CharField(max_length=50, unique=True, verbose_name='Código de la especialidad médica')
    nombre = models.CharField(max_length=200, verbose_name='Nombre de la especialidad médica')


    class Meta:
        db_table = 'especialidades'
    
    def __str__(self):
        return (f'{self.codigo}-{self.nombre}')
    
    