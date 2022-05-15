from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User
# Create your models here.



class Account(AbstractBaseUser):
    user =models.ForeignKey(User, on_delete=models.CASCADE)

    is_admin = models.BooleanField(default = False)
    is_professor = models.BooleanField(default = False)
    is_Monitor = models.BooleanField(default = False)
    is_aluno = models.BooleanField(default = True)

    def make_admin(self):
        is_admin = True
    def make_professor(self):
        is_professor = True

    def make_monitor(self):
        is_Monitor = True
    def make_aluno(self):
        is_aluno = True        