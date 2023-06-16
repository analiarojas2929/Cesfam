
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .models import CustomUsuario,TipoUsuario, Medico, Paciente, Farmaceutico, TipoMedicamento, Medicamento, Receta, DetalleReceta, Entrega, DetalleEntrega
from .forms import TipoUsuarioForm,CustomUsuarioForm, MedicoForm, PacienteForm, FarmaceuticoForm, TipoMedicamentoForm, MedicamentoForm, RecetaForm, DetalleRecetaForm, EntregaForm, DetalleEntregaForm


# Create your views here.

#registro
def login(request):
    return render(request,'core/registro/login.html')

def registro(request):
    return render(request,'core/registro/registro.html')



#//fin de registro


#farmaceutico



def menumedicamentos(request):
    return render(request,'core/farmaceutico/menumedicamentos.html')

def registromedicamento(request):
    return render(request,'core/farmaceutico/registromedicamento.html')   

def retiromedicamento(request):
    return render(request,'core/farmaceutico/retiromedicamento.html') 

def stock(request):
    return render(request,'core/farmaceutico/stock.html')

def menufarmaceutico(request):
    return render(request,'core/farmaceutico/menufarmaceutico.html')

#fin de farmaceutico


#medic

def ajustes(request):
    return render(request,'core/medico/ajustes.html')

def buscar(request):
    return render(request,'core/medico/buscar.html')

def inventario(request):
    return render(request,'core/medico/inventario.html')   

def menu(request):
    return render(request,'core/medico/menu.html')

def perfil(request):
    return render(request,'core/medico/perfil.html')

def menuprescripcion(request):
    return render(request,'core/medico/menuprescripcion.html')

def menureserva(request):
    return render(request,'core/medico/menureserva.html')



#fin de medico


#paciente

def tomahora(request):
    return render(request,'core/paciente/tomahora.html')

#fin paciente


#Creacion Admin ------------------------------------------------------------------

def admin_creacion(request):
    return render(request,'core/admin/admin_creacion.html')