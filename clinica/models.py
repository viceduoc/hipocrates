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

class Seguro(models.Model):
    idSeguro = models.IntegerField(primary_key=True, verbose_name="ID seguro")
    seguro = models.CharField(max_length=60, verbose_name="nombre seguro")

    def __str__(self):
        return self.seguro

class Paciente(models.Model):
    idPaciente = models.IntegerField(primary_key=True, verbose_name="id paciente")
    rut = models.IntegerField(max_length=12, verbose_name="rut del paciente")
    nombre = models.CharField(max_length=80, verbose_name="nombre del paciente")
    correo = models.CharField(max_length=60, verbose_name="email del paciente")
    password =models.CharField(max_length=8, verbose_name="password del paciente")
    debe_actualizar = models.BooleanField(verbose_name="contraseña provisoria")
    seguro = models.ForeignKey(Seguro, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    idReserva = models.IntegerField(primary_key=True, verbose_name="ID reserva")
    fechaHoraReserva = models.DateTimeField(verbose_name="Fecha reserva")
    estaConfirmada = models.BooleanField(verbose_name="Está confirmada?")
    estaCompletada = models.BooleanField(verbose_name="Está completada?")
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

    def __str__(self):
        return self.funcionario + " " + self.paciente






