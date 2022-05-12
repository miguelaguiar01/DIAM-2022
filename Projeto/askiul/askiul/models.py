from tkinter import CASCADE
from django.conf import UserSettingsHolder
from django.contrib.auth.models import AbstractUser
from django.db import models

from django.contrib.auth.models import User

# Create your models here.



class Cadeira(models.Model):
    name = models.CharField(max_length=200)
    descrição = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    


class Curso(models.Model):
    NomeCurso = models.CharField(max_length=100, unique=True)
    Sigla = models.CharField(max_length=10,unique=True)
    def __str__(self):
        return self.Sigla

class Associar(models.Model):
    Curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    Cadeira = models.ForeignKey(Cadeira, on_delete=models.CASCADE)

class Aluno(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    Curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
