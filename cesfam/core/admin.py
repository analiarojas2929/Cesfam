
# Register your models here.

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUsuario

class CustomUsuarioAdmin(UserAdmin):
    pass

admin.site.register(CustomUsuario, CustomUsuarioAdmin)