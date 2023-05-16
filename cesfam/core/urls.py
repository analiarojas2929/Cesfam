
from django.urls import include, path
from . import views
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('',views.registro,name='registro'),
    path('inventario',views.inventario,name='inventario'),
    path('login',views.login,name='login'),
    path('menu',views.menu,name='menu'),
    path('buscar',views.buscar,name='buscar'),
    path('medicamentos',views.medicamentos,name='medicamentos'),
    path('ajustes',views.ajustes,name='ajustes'),
    path('perfil',views.perfil,name='perfil'),
    path('prescripcion',views.prescripcion,name='prescripcion'),
    path('reserva',views.reserva,name='reserva'),
]