from django.db import models

# Create your models here.


from django.core.exceptions import ValidationError
from django.db import models
import re

def validate_username(value):
    if not re.match("^[a-zA-Z0-9]+$", value):
        raise ValidationError("El nombre de usuario no debe contener signos.")
    
    if Usuario.objects.filter(user_name=value).exists():
        raise ValidationError("El nombre de usuario ya está en uso.")
    
    if not any(char.isdigit() for char in value):
        raise ValidationError("El nombre de usuario debe contener al menos un número.")
    
    if not any(char.isupper() for char in value):
        raise ValidationError("El nombre de usuario debe contener al menos una letra mayúscula.")
    
    if len(value) < 8 or len(value) > 20:
        raise ValidationError("El nombre de usuario debe tener entre 8 y 20 caracteres.")

def validate_password(value):
    if len(value) < 8:
        raise ValidationError("La contraseña debe tener al menos 8 caracteres.")

    if not any(char.isupper() for char in value):
        raise ValidationError("La contraseña debe contener al menos una letra mayúscula.")

    if ' ' in value:
        raise ValidationError("La contraseña no debe contener espacios.")

    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', value):
        raise ValidationError("La contraseña debe contener al menos un signo.")

def validate_identification(value):

    if len(value) != 10:
        raise ValidationError("La identificación debe tener 10 dígitos.")

    if not value.isdigit():
        raise ValidationError("La identificación debe contener solo números.")

    if re.search(r'(\d)\1{3}', value):
        raise ValidationError("La identificación no puede tener un mismo número repetido 4 veces seguidas.")

class Usuario(models.Model):
    id_usuario = models.ForeignKey
    user_name = models.CharField(validators=[validate_username])
    password = models.CharField(validators=[validate_password])
    email = models.EmailField(max_length=100)
    sesion_activa = models.BooleanField()


class Persona(models.Model):
    id_persona = models.ForeignKey
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    identificacion = models.CharField(validators=[validate_identification])
    fecha_nacimiento = models.DateField()


class Sesions(models.Model):
    fecha_ingreso = models.DateField()
    fecha_cierre = models.DateField()
    usuario_idUsuario = models.IntegerField()


class Rol(models.Model):
    rol_idRol = models.IntegerField()
    usuarios_idUsuarios = models.IntegerField()


class Rol_usuarios(models.Model):
    rol_idRol = models.IntegerField()
    Usuarios_idUsuario = models.IntegerField()


class Rol_opciones(models.Model):
    nombre_opcion = models.CharField(max_length=100)
    ide_opcion = models.IntegerField()


class Rol_RolOpciones(models.Model):
    rol_idRol = models.IntegerField()
    rol_name = models.CharField(max_length=100)