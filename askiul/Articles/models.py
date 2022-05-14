from django.db import models
from django.contrib.auth.models import User


#models



class Cadeira(models.Model):
    titulo=models.CharField(max_length=300)
    descricao=models.CharField(max_length=300)
    image = models.ImageField(default="askiul\assets\default.png",upload_to='images')
    
    def __str__(self):
        return self.titulo
class Questao(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    #Cadeira =models.ForeignKey(Cadeira, on_delete=models.CASCADE)
    titulo=models.CharField(max_length=300)
    slug=models.SlugField()
    questao=models.TextField()
    add_time= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
class Resposta(models.Model):
    questao = models.ForeignKey(Questao, on_delete=models.CASCADE)
    questao=models.TextField()
    slug=models.SlugField()
    add_time= models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.questao