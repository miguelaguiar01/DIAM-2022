from django.urls import path
from . import views
app_name ='accounts'

urlpatterns = [
    path('login', views.login, name= 'login'),
    path('logout/',views.logout,name= 'logout'),
    path('login_validate',views.login_validate,name= 'login_validate'),
    path('signup', views.signup,name = 'signup'),
    path('home', views.home, name= "home"),
    path('submitatribuiradmin', views.submitatribuiradmin, name= "submitatribuiradmin"),
    path('submitatribuirprofessor', views.submitatribuirprofessor, name= "submitatribuirprofessor"),
    path('submitatribuirmonitor', views.submitatribuirmonitor, name= "submitatribuirmonitor"),
    path('gestao', views.gestao, name= "gestao")
]
