from django.db import models

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