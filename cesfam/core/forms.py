from django import forms
from .models import CustomUsuario,TipoUsuario, Medico, Paciente, Farmaceutico, TipoMedicamento, Medicamento, Receta, DetalleReceta, Entrega, DetalleEntrega

class CustomUsuarioForm(forms.ModelForm):
    class Meta:
        model = CustomUsuario
        fields = ('username', 'email', 'password', 'id_tipo_usuario')


class TipoUsuarioForm(forms.ModelForm):
    class Meta:
        model = TipoUsuario
        fields = ('nombre_tipo_usuario', 'descripcion')
class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ['id_medico','nombre_medico','especialidad','correo_electronico','telefono','id_tipo_usuario']

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['id_paciente','nombre_paciente','apellido_paciente','fecha_nacimiento','direccion','correo_electronico','telefono']

class FarmaceuticoForm(forms.ModelForm):
    class Meta:
        model = Farmaceutico
        fields = ['id_farmaceutico','nombre_farmaceutico','apellido_farmaceutico','correo_electronico','telefono','id_tipo_usuario']

class TipoMedicamentoForm(forms.ModelForm):
    class Meta:
        model = TipoMedicamento
        fields = ['id_tipo_medicamento','nombre_tipo_medicamento','descripcion']

class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = ['id_medicamento','nombre_medicamento','descripcion','stock','fecha_vencimiento','id_tipo_medicamento']

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['id_receta','id_medico','id_paciente','fecha']

class DetalleRecetaForm(forms.ModelForm):
    class Meta:
        model = DetalleReceta
        fields = ['id_detalle_receta','id_receta','id_medicamento','dosis','frecuencia']

class EntregaForm(forms.ModelForm):
    class Meta:
        model = Entrega
        fields = ['id_entrega','id_receta','id_paciente','fecha_entrega']

class DetalleEntregaForm(forms.ModelForm):
    class Meta:
        model = DetalleEntrega
        fields = ['id_detalle_entrega','id_entrega','id_medicamento','cantidad_entregada']
