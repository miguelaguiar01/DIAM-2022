from django.urls import path, include
from . import views
app_name ='articles'

urlpatterns = [
    path('<int:cadeira_id>', views.cadeira, name= 'cadeira'),
    path('Accounts',include("Accounts.urls")),
    path('home', views.home, name= "home")


]