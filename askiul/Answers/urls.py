from django.urls import path, include
from . import views
app_name ='answers'

urlpatterns = [
    
    path('<int:questao_id>', views.questao, name= 'questao'),
    
    path('Accounts',include("Accounts.urls")),
    path('home', views.home, name= "home")


]