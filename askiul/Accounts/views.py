from django.shortcuts import render,HttpResponseRedirect,reverse
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.http import HttpResponse
from Articles.models import Questao, Resposta, Cadeira
from .models import Account
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    cadeiras = Cadeira.objects.all()
    return render(request, "home.html",{'cadeiras':cadeiras})
def login(request):
    return render(request, 'login.html')

def login_validate(request):
    if(request.POST):
        login_data = request.POST.dict()
        username = login_data.get("name")
        password = login_data.get("password")
        user = authenticate(username=username, password=password)
        django_login(request, user)
        return HttpResponseRedirect(reverse('accounts:home'))
     
def signup(request):
    if(request.POST):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username, email, password)
        account = Account(user=user)
        account.save()
        django_login(request, user)
        return HttpResponseRedirect(reverse('accounts:home'))
    else:
        return render(request, "signup.html")
def gestao(request):
    users = User.objects.all()
    return render(request, "gestao.html",{'users':users})
def submitatribuiradmin(request):
    u = request.POST['user']
    user = User.objects.get(username=u)
    account = Account.objects.get(user=user)
    account.make_admin()
    account.save()
    return HttpResponseRedirect(reverse('accounts:home'))
def submitatribuirprofessor(request):
    u = request.POST['user']
    user = User.objects.get(username=u)
    account = Account.objects.get(user=user)
    account.make_professor()
    account.save()
    return HttpResponseRedirect(reverse('accounts:home'))
def submitatribuirmonitor(request):
    u = request.POST['user']
    user = User.objects.get(username=u)
    account = Account.objects.get(user=user)
    account.make_monitor()
    account.save()
    return HttpResponseRedirect(reverse('accounts:home'))
def logout(request):
        django_logout(request)
        cadeiras = Cadeira.objects.all()
        return HttpResponseRedirect(reverse('accounts:home'))
    