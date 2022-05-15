from django.shortcuts import render,  get_object_or_404
from Articles.models import Questao, Resposta, Cadeira
from django.shortcuts import redirect,HttpResponseRedirect,reverse
# Create your views here.


def cadeira(request, cadeira_id):
    cadeira = get_object_or_404(Cadeira, pk= cadeira_id)
    return render(request, 'question.html',{'cadeira':cadeira})

def home(request):
    cadeiras = Cadeira.objects.all()
    return render(request, "home.html",{'cadeiras':cadeiras})


def criar_questao(request,cadeira_id):
    cadeira = get_object_or_404(Cadeira, pk= cadeira_id)
    if request.method == 'POST':
        try:
                new_question = Questao(request.user,cadeira,titulo=request.POST['question'])
                questao_texto = new_question.titulo
        except KeyError:
            return render(request, 'criar_questao.html',{'cadeira':cadeira} )
        if questao_texto is not None:
            questao = Questao(user = request.user,cadeira= cadeira,titulo=questao_texto)
            questao.save()
            return HttpResponseRedirect(reverse('articles:cadeira', args=str(cadeira_id)))
        else:
            return render(request, 'criar_questao.html',{'cadeira':cadeira} )
    else:
        return render(request, 'criar_questao.html',{'cadeira':cadeira} )


def criar_cadeira(request):
    if request.method == 'POST':
        try:
                new_cadeira = Cadeira(titulo=request.POST['titulo'],descricao=request.POST['descricao'])
                cadeira_texto = new_cadeira.titulo
        except KeyError:
            return render(request, 'criar_cadeira.html' )
        if cadeira_texto is not None:
            cadeira = Cadeira(titulo=request.POST['titulo'],descricao=request.POST['descricao'])
            cadeira.save()
            cadeiras = Cadeira.objects.all()
            return HttpResponseRedirect(reverse('articles:home'))
        else:
            return render(request, 'criar_cadeira.html')
    else:
        return render(request, 'criar_cadeira.html')



def delete_cadeira(request, cadeira_id):
    cadeira = get_object_or_404(Cadeira, pk= cadeira_id)
    cadeira.delete()
    cadeiras = Cadeira.objects.all()
    return HttpResponseRedirect(reverse('articles:home'))