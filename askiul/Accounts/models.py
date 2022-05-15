from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
# Create your models here.



class Account(AbstractBaseUser):
    user =models.ForeignKey(User, on_delete=models.CASCADE)

    is_admin = models.BooleanField(default = False)
    is_professor = models.BooleanField(default = False)
    is_Monitor = models.BooleanField(default = False)
    is_aluno = models.BooleanField(default = True)
    uid = models.UUIDField(
        default=None,
        blank=True,
        null=True,
        unique=True,
    )

    USERNAME_FIELD = "uid"
    #my_group = Group.objects.get(name='Aluno') 
    ##my_group.user_set.add(user.id)
    def __str__(self):
        return "user.name"
    def make_admin(self):
        self.is_admin = True
        
    def make_professor(self):
        self.is_professor = True
        ##my_group = Group.objects.get(name='Monitor') 
        ##my_group.user_set.add(user)
    def make_monitor(self):
        self.is_Monitor = True
        #my_group = Group.objects.get(name='Professor') 
        #my_group.user_set.add(user)
    def make_aluno(self):
        self.is_aluno = True        