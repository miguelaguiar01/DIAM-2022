from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
def home(request):
    #return HttpResponse('home') 
    return render(request, 'home.html')


def login_go(request):
    return HttpResponseRedirect('registration/login.html')