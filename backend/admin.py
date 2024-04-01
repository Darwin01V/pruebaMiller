from django.contrib import admin
from backend.models import *

# Register your models here.

#class Usuario(admin.ModelAdmin):
#    list_display = ('id', 'nombre', 'apellidos', 'email')

admin.site.register(Usuario)
admin.site.register(Persona)
admin.site.register(Sesions)
admin.site.register(Rol)
admin.site.register(Rol_usuarios)
admin.site.register(Rol_opciones)
admin.site.register(Rol_RolOpciones)