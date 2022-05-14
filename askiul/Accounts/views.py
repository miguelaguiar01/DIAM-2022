from django.shortcuts import render
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.http import HttpResponse
from Articles.models import Questao, Resposta, Cadeira
from .forms import RegistrationForm
# Create your views here.


def login(request):
    return render(request, 'login.html')

def login_validate(request):
    if(request.POST):
        login_data = request.POST.dict()
        username = login_data.get("name")
        password = login_data.get("password")
        user = authenticate(username=username, password=password)
        django_login(request, user)
        cadeiras = Cadeira.objects.all()
        return render(request, "home.html", {'cadeiras':cadeiras})
     
def signup_validate(request):
    if(request.POST):
        form = RegistrationForm(request.POST)
        print(form)
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        django_login(request, user)
        cadeiras = Cadeira.objects.all()
        return render(request, "home.html", {'cadeiras':cadeiras})
    else:
        form = UserCreationForm()
    return render(request, 'signup.html',{'form':form})
    
def signup(request):
    
    if(request.POST):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
        
    return render(request, 'signup.html',{'form': form})

def logout(request):
        django_logout(request)
        cadeiras = Cadeira.objects.all()
        return render(request, "home.html", {'cadeiras':cadeiras})
    