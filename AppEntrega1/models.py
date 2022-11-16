from django.db import models

# Create your models here.

class ProfesoresCoder(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    materia = models.CharField(max_length=40)

class TutoresCoder(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    materia = models.CharField(max_length=40)

class AlumnosCoder(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    materia = models.CharField(max_length=40)
