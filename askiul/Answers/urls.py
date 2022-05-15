from django.urls import path, include
from . import views
app_name ='answers'

urlpatterns = [
    
    path('<int:questao_id>', views.questao, name= 'questao'),
    path('questao',views.questao, name="questao"),
    path('Accounts',include("Accounts.urls")),
    path('home', views.home, name= "home"),
    path('<int:questao_id>/criar_resposta', views.criar_resposta, name="criar_resposta"),
    


]