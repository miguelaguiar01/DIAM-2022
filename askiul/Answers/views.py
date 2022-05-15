from django.shortcuts import render,  get_object_or_404
from Articles.models import Questao, Resposta, Cadeira

# Create your views here.
def questao(request, questao_id):
    questao = get_object_or_404(Questao, pk= questao_id)
    return render(request, 'answer.html',{'questao':questao})

def home(request):
    cadeiras = Cadeira.objects.all()
    return render(request, "home.html",{'cadeiras':cadeiras})


def criar_resposta(request,questao_id):
    questao = get_object_or_404(Questao, pk= questao_id)
    if request.method == 'POST':
        try:
                new_answer = Resposta(user = request.user,questao = questao,titulo=request.POST['title'],resposta=request.POST['resposta'])
                resposta_titulo = new_answer.titulo
                resposta_texto = new_answer.resposta
        except KeyError:
            return render(request, 'criar_resposta.html',{'questao':questao} )
        if resposta_texto is not None:
            resposta = Resposta(user = request.user,questao= questao,titulo=resposta_titulo,resposta =resposta_texto)
            resposta.save()
            return render(request, 'answer.html',{'questao':questao})
        else:
            return render(request, 'criar_resposta.html',{'questao':questao} )
    else:
        return render(request, 'criar_resposta.html',{'questao':questao} )