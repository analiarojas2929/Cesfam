from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#registro
def login(request):
    return render(request,'core/registro/login.html')

def registro(request):
    return render(request,'core/registro/registro.html')



#//fin de registro


#farmaceutico



def medicamentos(request):
    return render(request,'core/farmaceutico/medicamentos.html')

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

def prescripcion(request):
    return render(request,'core/medico/prescripcion.html')

def reserva(request):
    return render(request,'core/medico/reserva.html')



#fin de medico


#paciente

def tomahora(request):
    return render(request,'core/paciente/tomahora.html')

#fin paciente