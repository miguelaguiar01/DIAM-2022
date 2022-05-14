from django.shortcuts import render,  get_object_or_404
from Articles.models import Questao, Resposta, Cadeira

# Create your views here.
def questao(request, questao_id):
    questao = get_object_or_404(Questao, pk= questao_id)
    return render(request, 'answer.html',{'questao':questao})

def home(request):
    cadeiras = Cadeira.objects.all()
    return render(request, "home.html",{'cadeiras':cadeiras})