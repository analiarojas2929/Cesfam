from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class TipoUsuario(models.Model):
    id_tipo_usuario = models.IntegerField(primary_key=True)
    nombre_tipo_usuario = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre_tipo_usuario


class CustomUsuario(AbstractUser):
    id_tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)
    groups = models.ManyToManyField(Group, related_name='custom_users')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_users')

    def __str__(self):
        return self.username


class Medico(models.Model):
    id_medico = models.IntegerField(primary_key=True)
    nombre_medico = models.CharField(max_length=255)
    especialidad = models.CharField(max_length=255)
    correo_electronico = models.EmailField(max_length=255)
    telefono = models.CharField(max_length=255)
    id_tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_medico


class Paciente(models.Model):
    id_paciente = models.IntegerField(primary_key=True)
    nombre_paciente = models.CharField(max_length=255)
    apellido_paciente = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=255)
    correo_electronico = models.EmailField(max_length=255)
    telefono = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre_paciente


class Farmaceutico(models.Model):
    id_farmaceutico = models.IntegerField(primary_key=True)
    nombre_farmaceutico = models.CharField(max_length=255)
    apellido_farmaceutico = models.CharField(max_length=255)
    correo_electronico = models.EmailField(max_length=255)
    telefono = models.CharField(max_length=255)
    id_tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_farmaceutico


class TipoMedicamento(models.Model):
    id_tipo_medicamento = models.IntegerField(primary_key=True)
    nombre_tipo_medicamento = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre_tipo_medicamento


class Medicamento(models.Model):
    id_medicamento = models.IntegerField(primary_key=True,default=0)
    nombre_medicamento = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255, default='Descripción por defecto')
    stock = models.IntegerField(default=0)
    fecha_vencimiento = models.DateField(null=True, blank=True)
    id_tipo_medicamento = models.ForeignKey(TipoMedicamento, on_delete=models.CASCADE,default=0)

    def __str__(self):
        return self.nombre_medicamento


class Receta(models.Model):
    id_receta = models.IntegerField(primary_key=True)
    id_medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha = models.DateField()

    def __str__(self):
        return f"Receta #{self.id_receta}"


class DetalleReceta(models.Model):
    id_detalle_receta = models.IntegerField(primary_key=True)
    id_receta = models.ForeignKey(Receta, on_delete=models.CASCADE)
    id_medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE,null=True, blank=True)
    dosis = models.CharField(max_length=255)
    frecuencia = models.CharField(max_length=255)

    def __str__(self):
        return f"Detalle Receta #{self.id_detalle_receta}"


class Entrega(models.Model):
    id_entrega = models.IntegerField(primary_key=True)
    id_receta = models.ForeignKey(Receta, on_delete=models.CASCADE)
    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha_entrega = models.DateField()

    def __str__(self):
        return f"Entrega #{self.id_entrega}"


class DetalleEntrega(models.Model):
    id_detalle_entrega = models.IntegerField(primary_key=True)
    id_entrega = models.ForeignKey(Entrega, on_delete=models.CASCADE)
    id_medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE,null=True, blank=True)
    cantidad_entregada = models.IntegerField()

    def __str__(self):
        return f"Detalle Entrega #{self.id_detalle_entrega}"
