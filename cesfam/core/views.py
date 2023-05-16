from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def registro(request):
    return render(request,'core/registro.html')


def login(request):
    return render(request,'core/login.html')

def menu(request):
    return render(request,'core/menu.html')

def inventario(request):
    return render(request,'core/inventario.html')
    
def buscar(request):
    return render(request,'core/buscar.html')

def medicamentos(request):
    return render(request,'core/medicamentos.html')

def perfil(request):
    return render(request,'core/perfil.html')

def prescripcion(request):
    return render(request,'core/prescripcion.html')

def reserva(request):
    return render(request,'core/reserva.html')

def ajustes(request):
    return render(request,'core/ajustes.html')
