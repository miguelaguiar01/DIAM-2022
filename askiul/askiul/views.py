from django.http import HttpResponse
from django.shortcuts import render
from Articles.models import Questao, Resposta
def home(request):
    questoes = Questao.objects.all()
    return render(request, "home.html", {'questoes':questoes})
