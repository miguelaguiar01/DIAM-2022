from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
def home(request):
    #return HttpResponse('home') 
    return render(request, 'home.html')

def showLogin(request):
    return render(request, 'registration/login.html')

def login_validate(request):
    if(request.POST):
        login_data = request.POST.dict()
        username = login_data.get("name")
        password = login_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('/')    
    return HttpResponseRedirect('registration/login.html')

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
        
    return render(request, 'registration/signup.html', {'form': form})