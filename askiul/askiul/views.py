from django.http import HttpResponse
from django.shortcuts import render
from Articles.models import Questao, Resposta, Cadeira
def home(request):
    cadeiras = Cadeira.objects.all()
    return render(request, "home.html",{'cadeiras':cadeiras})
