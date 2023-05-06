
from django.urls import include, path
from . import views
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('',views.registro,name='registro'),
    path('login',views.login,name='login'),
    path('menu',views.menu,name='menu'),
    path('inventario',views.inventario,name='inventario'),
    path('buscar',views.buscar,name='buscar'),
    path('medicamentos',views.medicamentos,name='medicamentos'),
]