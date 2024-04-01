from django.db import models

# Create your models here.


class Usuario(models.Model):
    id_usuario = models.ForeignKey
    user_name = models.CharField(max_length=10)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    sesion_activa = models.BooleanField()


class Persona(models.Model):
    id_persona = models.ForeignKey
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    identificaacion = models.IntegerField()
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