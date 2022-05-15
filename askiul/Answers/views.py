from django.shortcuts import render,  get_object_or_404,HttpResponseRedirect,reverse
from Articles.models import Questao, Resposta, Cadeira
from django.contrib.auth.decorators import login_required, permission_required

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
                new_answer = Resposta(user = request.user,questao = questao,titulo=request.POST['title'])
                resposta_titulo = new_answer.titulo
                resposta_texto = new_answer.resposta
        except KeyError:
            return render(request, 'criar_resposta.html',{'questao':questao} )
        if resposta_texto is not None:
            resposta = Resposta(user = request.user,questao= questao,titulo=resposta_titulo, resposta= resposta_texto)
            resposta.save()
            return HttpResponseRedirect(reverse('answers:questao', args=str(questao_id)))
        else:
            return render(request, 'criar_resposta.html',{'questao':questao} )
    else:
        return render(request, 'criar_resposta.html',{'questao':questao} )