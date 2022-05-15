from django.urls import path
from . import views
app_name ='accounts'

urlpatterns = [
    path('login', views.login, name= 'login'),
    path('logout/',views.logout,name= 'logout'),
    path('login_validate',views.login_validate,name= 'login_validate'),
    path('signup', views.signup,name = 'signup')
]
