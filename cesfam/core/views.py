from django.shortcuts import render
from django.http import HttpResponse
from .models import Entrega_medicamentos, Entrega_pendiente, Paciente, CustomUsuario, Personal, Medicamento, Receta_medica
from django.contrib.auth import authenticate, login, logout
from .forms import creacion_personal, creacion_receta, modificar_stock

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
    if request.POST:
        form = creacion_personal(request.POST, request.FILES)
        if form.is_valid():

            sexo_personal = form.data.get('sexo_personal')
            if sexo_personal == 'is_masc':
                personal = Personal(run_personal = form.cleaned_data.get('run_personal'),
                dv_personal = form.cleaned_data.get('dv_personal'),
                nombre_personal = form.cleaned_data.get('nombre_personal'),
                apellido_personal = form.cleaned_data.get('apellido_personal'),
                mail_personal = form.cleaned_data.get('mail_personal'),
                is_masculino = True,
                edad_personal = form.cleaned_data.get('edad_personal'),
                tipo = form.cleaned_data.get('tipo'))
            else:
                personal = Personal(run_personal = form.cleaned_data.get('run_personal'),
                dv_personal = form.cleaned_data.get('dv_personal'),
                nombre_personal = form.cleaned_data.get('nombre_personal'),
                apellido_personal = form.cleaned_data.get('apellido_personal'),
                mail_personal = form.cleaned_data.get('mail_personal'),
                is_femenino = True,
                edad_personal = form.cleaned_data.get('edad_personal'),
                tipo = form.cleaned_data.get('tipo'))

            nombre = form.cleaned_data.get('nombre_personal')
            apellido = form.cleaned_data.get('apellido_personal')
            run = form.cleaned_data.get('run_personal')
            dv = form.cleaned_data.get('dv_personal')
            tipo = form.cleaned_data.get('tipo')

            if tipo == 'is_farm':
                user = CustomUsuario.objects.create_user(username = nombre[0:2] + '.' + apellido,
                password = apellido[0].capitalize() + str(run) + '-' + str(dv),
                is_farmaceutico = True)
                user.save()
                personal.save()
            elif tipo == 'is_med':
                user = CustomUsuario.objects.create_user(username = nombre[0:2] + '.' + apellido,
                password = apellido[0].capitalize() + str(run) + '-' + str(dv),
                is_medico = True)
                user.save()
                personal.save()
            elif tipo == 'is_adm':
                user = CustomUsuario.objects.create_user(username = nombre[0:2] + '.' + apellido,
                password = apellido[0].capitalize() + str(run) + '-' + str(dv),
                is_admin = True)
                user.save()
                personal.save()

            messages.success(request, 'Usuario creado correctamente, su cuenta: \nnombre: ' + nombre[0:2] + '.' + apellido +
            '\ncontraseña: '+ apellido[0].capitalize() + str(run) + '-' + str(dv))

    return render(request, 'admin/admin_creacion.html', {'form': creacion_personal})