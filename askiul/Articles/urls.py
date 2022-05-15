from django.urls import path, include
from . import views
app_name ='articles'

urlpatterns = [
    path('<int:cadeira_id>', views.cadeira, name= 'cadeira'),
    path('Answers',include("Answers.urls")),
    path('Accounts',include("Accounts.urls")),
    path('home', views.home, name= "home"),
    path('<int:cadeira_id>/criar_questao', views.criar_questao, name="criar_questao"),
    path('criar_cadeira', views.criar_cadeira, name= "criar_cadeira"),
    path('<int:cadeira_id>/delete_cadeira',views.delete_cadeira, name="delete_cadeira")
]