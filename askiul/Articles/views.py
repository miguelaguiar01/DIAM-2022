from django.shortcuts import render,  get_object_or_404
from Articles.models import Questao, Resposta, Cadeira
# Create your views here.


def cadeira(request, cadeira_id):
    cadeira = get_object_or_404(Cadeira, pk= cadeira_id)
    return render(request, 'question.html',{'cadeira':cadeira})

def home(request):
    cadeiras = Cadeira.objects.all()
    return render(request, "home.html",{'cadeiras':cadeiras})