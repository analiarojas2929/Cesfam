from django.db import models

# Create your models here.

class Medicamento(models.Model):
    nombre_medicamento = models.CharField(max_length=25)
    fecha_elab_medicamento = models.DateField(null=True)
    fecha_venc_medicamento = models.DateField(null=True)
    cantidad_medicamento = models.CharField(max_length=4)

    def __str__(self):
        return self.nombre_medicamento
