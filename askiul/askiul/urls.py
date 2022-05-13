
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Accounts',include("Accounts.urls")),
    path('home/',views.home),
    path('', views.home)
]

urlpatterns += staticfiles_urlpatterns()