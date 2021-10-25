from django.db import models
from django.db.models.base import Model

# Create your models here.

class TipoFuncionario(models.Model):
    idTipofuncionario = models.IntegerField(primary_key=True,verbose_name="ID tipo Funcionario")
    tipoFuncionario = models.CharField(max_length=60, verbose_name="Tipo Funcionario")

    def __str__(self):
        return self.tipoFuncionario

class Especialidad(models.Model):
    idEspecialidad = models.IntegerField(primary_key=True,verbose_name="ID especialidad")
    especialidad = models.CharField(max_length=60, verbose_name="Tipo Especialidad")

    def __str__(self):
        return self.especialidad

class Funcionario(models.Model):
    idFuncionario = models.IntegerField(primary_key=True,verbose_name="ID funcionario")
    rut = models.CharField(max_length=12, verbose_name="rut funcionario")
    nombre = models.CharField(max_length=80, verbose_name="nombre funcionario")
    correo = models.CharField(max_length=60, verbose_name="email funcionario")
    password =models.CharField(max_length=8, verbose_name="password")
    debe_actualizar = models.BooleanField(verbose_name="contraseña provisoria")
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    tipoFuncionario = models.ForeignKey(TipoFuncionario,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

